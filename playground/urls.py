from django.urls import path
from . import views


#URLConf
urlpatterns=[
    path('hello/',views.say_hello) #note we didn't pay in the fuction say_hello()
                                             #rather we passed a reference to it say_hello
    #path(give it a route or url, and a view function)                                         
]