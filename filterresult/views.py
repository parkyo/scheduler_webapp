from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib.request
from bs4 import BeautifulSoup
from .models import Section, Class
from scheduler.models import Input
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def resultView(request):

    url = 'https://atlas.ai.umich.edu/course/AAS%20103/'

    # DP = "C:/Users/shinlopark/Downloads/chromedriver"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get(url)
    text = driver.find_element_by_class_name('text-large')

    # session = HTMLSession()
    # response = session.get(url)
    # soup = BeautifulSoup(response.content, 'html.parser')
    
    # str_print = []
    # inputs = Input.objects.all()
    # soup = BeautifulSoup(urllib.request.urlopen(url))
    # container = soup.find('div', attrs={'class': "course-sections-availability-container"})
    # text = container.find('h2', attrs={'class':'text-med'}).text


    # if inputs :

    #     for a in inputs:
    #         course = ""
    #         num = ""
    #         for i in range(0, len(a.text)-3):
    #             course += a.text[i]
            
    #         for i in range(len(a.text)-3, len(a.text)):
    #             num += a.text[i]

    #         final_url = f"{url}{course}%20{num}/"
    #         name = course + num

    #         # response = requests.get(final_url)
    #         soup = BeautifulSoup(urllib.request.urlopen(final_url))
    #         container = soup.find_all('div', attrs={'class':'nav-bar-container'})
    #         text = container[0].find('h1', attrs={'class':'text-large'})
    #         str_print.append(text)
    
    return render(request, 'filterresult.html', {'str':text})


    