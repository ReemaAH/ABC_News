from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import News


def index(request):
    latest_news_list = News.objects.order_by('pub_date')[:2]
    popular_news_list = News.objects.filter(popular=True)[:4]
    template = loader.get_template('newsapp/homepage.html')
    context = {
       'latest_news_list': latest_news_list,
       'popular_news_list': popular_news_list,
    }
    return HttpResponse(template.render(context, request))


def tech(request):
    items= News.objects.filter(category="tech")
    template = loader.get_template('newsapp/tech.html')
    context = {
       'items': items,
    }
    return HttpResponse(template.render(context, request))

def art(request):
    items= News.objects.filter(category="art")
    template = loader.get_template('newsapp/art.html')
    context = {
       'items': items,
    }
    return HttpResponse(template.render(context, request))
    

def Sci(request):
    items= News.objects.filter(category="Sci")
    template = loader.get_template('newsapp/Sci.html')
    context = {
       'items': items,
    }
    return HttpResponse(template.render(context, request))
    

def business(request):
    items= News.objects.filter(category="business")
    template = loader.get_template('newsapp/business.html')
    context = {
       'items': items,
    }
    return HttpResponse(template.render(context, request))

def newsdetails(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request, 'newsapp/newsContent.html', {'news': news})

def search(request):        
    query =  request.GET.get('search') 
    object_list =  News.objects.filter(title__icontains=query)      
    return render(request,"newsapp/search.html", {"news":object_list})


def subscribe(request):
    return render(request,"newsapp/subscribe.html")


def subform(request):
    query =  request.GET.get('email') 
    message= "Thank you for subscribing with ABC news.\n " + "You will recieve our news each weeks!"
    return render(request,'newsapp/subscribe.html', {"message": message})
    






