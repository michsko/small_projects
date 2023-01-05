from django.urls import path
from . import views

urlpatterns = [
	#int: 
	#str:
	#path: Urls/
	#slug: hyphen-and_underscores
	#UUID: uuid
	path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.event_list, name="event_list"),
    path('add_venue', views.add_venue, name="add_venue"),

]
   
