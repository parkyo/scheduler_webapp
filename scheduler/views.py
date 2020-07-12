from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import pandas as pd
from .models import Input

def schedulerView(request):
    # classnames=[]
    # Filters(dpt = request.POST['dpt'])
    return render(request, 'scheduler.html')

def getResult(request):
    # want to loop through inputs instead of repeating
    for i in range(0,4):
        name = 'class' + str(i)
        text = request.POST.get(name, False)
        if text :
            c = Input(text = text)
            c.save()
    
    return HttpResponseRedirect('/filterresult')

    



# def fetchFilters(self, request, classnames):
#     classname = Filters(classname = request.POST['classname'])
#     return HttpResponseRedirect('/filterresult')
    # return HttpResponse(credits.content)

    # return render(request, 'filterresult.html', {'dpt':dpt})

# def fetchFilteredClasses(request, dpt, classnames):
    # sections=[]
    
    # return HttpResponseRedirect('/filterresult')
    # for a in soup.findAll('div', attrs = {'class' : 'row toppadding_main bottompadding_interior'}):
    #     name = a.find('div', attrs={'class':'col-sm-12'})
    #     AASclasses.append(name.text)
    #     # sections.append(section.text)

    # df = pd.DataFrame({'Class Name':classnames}) 
    # df.to_csv('products.csv', index=False, encoding='utf-8')

# def fetchFilters():
