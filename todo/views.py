from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import TodoItem
from itertools import groupby
from django.utils.html import conditional_escape as esc
import calendar

def todoView(request):
    d = datetime.today()
    cal = calendar.month(d.year, d.month, 0, 1)
    # html_cal = cal.formatmonth(d.year, d.month)
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', 
    {'all_items' : all_todo_items, 'cal' : cal})


def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo')
    # create a new todo all_items
    #save
    #redirect the browser to '/todo/'

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


