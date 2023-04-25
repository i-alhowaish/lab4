from django.urls import path
from . import views
urlpatterns = [
    path("",views.empty,name='empty'),
    path("taxrate" , views.tax , name='tax'),
    path("<str:num>" , views.calc , name='calc')
    
]