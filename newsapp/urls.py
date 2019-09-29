from django.urls import path

from . import views




app_name = 'newsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('tech', views.tech, name='tech'),
    path('art', views.art, name='art'),
    path('Sci', views.Sci, name='Sci'),
    path('business', views.business, name='business'),
    path('<int:news_id>/', views.newsdetails, name='newsdetails'),
    path('search', views.search, name='search'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('subform', views.subform, name='subform'),
]
 # path('newsapp/homepage.html', views.index, name='index')
 


#app_name = 'polls'
#urlpatterns = [
   # path('', views.index, name='index'),
   # path('<int:question_id>/', views.detail, name='detail'),
   # path('<int:question_id>/results/', views.results, name='results'),
   # path('<int:question_id>/vote/', views.vote, name='vote'),
#]