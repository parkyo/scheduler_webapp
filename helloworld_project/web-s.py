# from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

classnames=[]
sections=[]
url = 'https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_20_2310&cgtype=ug&department=AAS&allsections=true&show=40'
response = requests.get(url)
# driver.get("https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_20_2310&cgtype=ug&show=20&dist=HU")

soup = BeautifulSoup(response.content,"html.parser")
for a in soup.findAll('div', attrs = {'class' : 'row toppadding_main bottompadding_interior'}):
    name = a.find('div', attrs={'class':'col-sm-12'})
    classnames.append(name.text)
    # sections.append(section.text)

df = pd.DataFrame({'Class Name':classnames}) 
df.to_csv('products.csv', index=False, encoding='utf-8')