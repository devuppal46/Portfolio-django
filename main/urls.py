from django.urls import path
from  main import views

urlpatterns=[
    path('projects/',views.projects, name= "projects"),
    path('languages/',views.languages,name= "languages" ),
    path('contact/',views.contact,name= "contact" ),
    path('',views.index, name= 'index' )
]