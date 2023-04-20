from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic is inserted successfully................')


    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WPO=WebpageForm()
    d={'WPO':WPO}


    if request.method=='POST':
        WPDO=WebpageForm(request.POST)
        if WPDO.is_valid():
            WPDO.save()
            return HttpResponse('webpage data is inserted successfully...........')



    return render(request,'insert_webpage.html',d)


def insert_access(request):
    ARFO=accessForm()
    d={'ARFO':ARFO}


    if request.method=='POST':
        ARDO=accessForm(request.POST)
        if ARDO.is_valid():
            ARDO.save()
            return HttpResponse('access data is inserted successfully.............')




            
    return render(request,'insert_access.html',d)

