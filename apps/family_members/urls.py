# we need the path
from django.urls import path
from . import views

# Django recognaises pth urls when there are 
# definne in the variable urlpatterens

app_name = 'FamMem-urls' # is is comming urls in settings 
urlpatterns = [
    path('', views.home_page, name='home-page')

]