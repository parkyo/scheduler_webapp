from django.shortcuts import render
from scheduler.models import Filters


def resultView(request):
    classname = Filters.classname
    # url = 'https://atlas.ai.umich.edu/course/AERO%20101/'
    # response = requests.get(url)
    # soup = BeautifulSoup(response.content,"html.parser")
    # median = soup.find('p', attrs={'class' : 'grade-median text-small bold'})
    # dpt = Filters(dpt = request.POST['dpt'])
    return render(request, 'filterresult.html', {'name': classname})