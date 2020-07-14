from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Section, Class
from scheduler.models import Input
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def resultView(request):
    fetchData()
    secs = Class.objects.all()
    return render(request, 'filterresult.html', {'str':secs})


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
            cur_c = Class(name=name)
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
    
    panel = soup.find('div', attrs={'id':'classScheduleBody'})
    secs = panel.find_all('div', attrs={'class':'row clsschedulerow toppadding_main bottompadding_main'})
    # str_print = []
    for sec in secs:
        type_texts = soup.find('div', {'class':'hidden-md hidden-lg xs_label'}, text = 'Class No:').next_sibling
        class_type = type_texts.split(" ")
        if class_type[1] == "(LAB)":
            break
        # cols = sec.find_all('div', attrs={'class':'col-md-1'})
        # text_node = cols[2].find_element_by_xpath("//div[@class='col-md-1']/text()")
        # no = cols[2].execute_script("return arguments[0].nextSibling.textContent;", text_node)  
        no = soup.find('div', {'class':'hidden-md hidden-lg xs_label'}, text = 'Class No:').next_sibling

        table = sec.find('div', attrs={'class':'col-md-4'})

        day = table.find('td', attrs={'class':'MPCol_Day'}).text
        # str_print.append(day)


        time = table.find('td', attrs={'class':'MPCol_Time'}).text
        # str_print.append(time)
        time_range = time.split(" - ", 1)
        start = time_range[0]
        end = time_range[1]
        if start[2] == ':':
            start = start.replace(' ', ' 0')
        if start[2] == ':':
            end = end.replace(" ", "0")

        start = datetime.strptime(start, " %I:%M%p")
        end = datetime.strptime(end,"%I:%M%p")
        cur_sec = Section(num=no, start_time=start, end_time=end, days=day)
        cur_sec.save()
        cur_class.section.add(cur_sec)

    
    
