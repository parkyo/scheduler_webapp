from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Section, Class, Day
from scheduler.models import Input
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

all_secs = []
schedule = [[0 for x in range(20)] for y in range(5)] 


def resultView(request):
    fetchData()
    makeSchedule(0)
    # classes = Class.objects.all()
    # i = 0
    # for i in range(0, 5):
    #     secs = Class.objects.filter(name=classes[i].name).section.all()
    #     all_secs.append(secs)
    #     i += 1

    # makeSchedule(0)
    return render(request, 'filterresult.html', {'str':schedule})


def fetchData():
    inputs = Input.objects.all()
    options = Options()
    options.add_argument('--headless')
    url = 'https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2310'
    if inputs :
        for a in inputs:
            course = ""
            num = ""
    
            for i in range(0, len(a.text)-3):
                course += a.text[i]
            
            for i in range(len(a.text)-3, len(a.text)):
                num += a.text[i]

            name = course + num
            cur_c = Class.objects.create(name=name)
            cur_c.save()
            final_url = f'{url}{name}001&termArray=f_20_2310/'
            driver = webdriver.Chrome(chrome_options=options)
            driver.get(final_url)
            response = driver.execute_script("return document.documentElement.outerHTML")
            driver.quit()
            soup = BeautifulSoup(response, "lxml")

            create_obj(soup, cur_c)
            
            cur_c.save()
            

def create_obj(soup, cur_class):
    sec_list = []
    panel = soup.find('div', attrs={'id':'classScheduleBody'})
    secs = panel.find_all('div', attrs={'class':'row clsschedulerow toppadding_main bottompadding_main'})
    # str_print = []
    for sec in secs:
        type_texts = sec.find_all('div', {'class':'col-md-1'})
        section = type_texts[0].find('span').text
        class_type = section.split(" ")
        if class_type[1] == "(LAB)" or class_type[1] == "(DIS)":
            break
        # cols = sec.find_all('div', attrs={'class':'col-md-1'})
        # text_node = cols[2].find_element_by_xpath("//div[@class='col-md-1']/text()")
        # no = cols[2].execute_script("return arguments[0].nextSibling.textContent;", text_node)  
        no = sec.find('div', {'class':'hidden-md hidden-lg xs_label'}, text = 'Class No:').next_sibling

        table = sec.find('div', attrs={'class':'col-md-4'})

        day = table.find('td', attrs={'class':'MPCol_Day'}).text
        
        time = table.find('td', attrs={'class':'MPCol_Time'}).text
        # str_print.append(time)
        time_range = time.split(" - ", 1)
        start = time_range[0]
        end = time_range[1]
        
        start.replace("\\D", "")

        times = start.split(":", 1)
        start = float(times[0])
        if start < 8 :
            start += 12

        if times[1] == '30AM' or times[1] == '30PM':
            start += 0.5

        times = end.split(":", 1)
        end = float(times[0])

        if end < 8 :
            end += 12

        if times[1] == '30AM' or times[1] == '30PM':
            end += 0.5

        cur_sec = Section(num=no, start_time=start, end_time=end)
        cur_sec.save()
        days = re.sub( r"([A-Z])", r" \1", day).split()
        for d in days:
            cur_day = Day.objects.create(day=d)
            cur_day.save()
            cur_sec.days.add(cur_day)

        cur_class.section.add(cur_sec)
        sec_list.append(cur_sec)

    all_secs.append(sec_list)
    
def makeSchedule(i):
    if (i < 0) or (i > 3):
        return True
    # if (sec > len(all_secs[0]) and sec > len(all_secs[1]) and sec > len(all_secs[2]) and sec > len(all_secs[3])):

    #     return False

    for sec in range(0, len(all_secs[i])):
        available = True
        days = all_secs[i][sec].days.all()
        diff = 8.0
        init_start = (all_secs[i][sec].start_time) - diff
        start = int(init_start / 0.5)
        end = int((all_secs[i][sec].end_time - diff) / 0.5)
        for d in days :
            if not available :
                break
            sec_day = 0
            
            if d.day == 'Tu' :
                sec_day = 1
            
            if d.day == 'W' :
                sec_day = 2
            
            if d.day == 'Th' :
                sec_day = 3
            
            if d.day == 'F' :
                sec_day = 4
            j = start

            while j < end :
                if schedule[sec_day][j] != 0 :
                    k = start
                    while k < j :
                        schedule[sec_day][k] = 0
                        k += 1
                    available = False
                    break
                schedule[sec_day][j] = all_secs[i][sec].num
                j += 1

        if available:
            break

    if makeSchedule(i+1):
            return True

            
        

    return False
