from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
import pandas as pd
from .models import Filters

def schedulerView(request):
    db = Filters.objects.all()
    return render(request, 'scheduler.html', {'dpt': db})


# def loadClasses(request, dpt):
#     fetchFilters(dpt)
#     return HttpResponseRedirect('/scheduler')

def fetchFilters(request):
    dpt = Filters(dpt = request.POST['dpt'])
    dpt.save()
    return HttpResponseRedirect('/scheduler')
    # return HttpResponse(credits.content)


def fetchFilteredClasses(dpt):
    classnames=[]
    # sections=[]
    # url = 'https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_20_2310&cgtype=ug&department=AAS&allsections=true&show=40'
    url = 'https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_20_2310&cgtype=ug&department={{dpt}}&allsections=true'
    response = requests.get(url)
    # driver.get("https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_20_2310&cgtype=ug&show=20&dist=HU")
    soup = BeautifulSoup(response.content,"html.parser")
    for a in soup.findAll('div', attrs = {'class' : 'row toppadding_main bottompadding_interior'}):
        name = a.find('div', attrs={'class':'col-sm-12'})
        classnames.append(name.text)
        # sections.append(section.text)

    # df = pd.DataFrame({'Class Name':classnames}) 
    # df.to_csv('products.csv', index=False, encoding='utf-8')

# def fetchFilters():
