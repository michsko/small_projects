from django.urls import path
from .import views

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
    path('venues', views.venues, name="venues"),
    path('show_venues/<venue_id>', views.show_venue, name='show_venue'),
    path('search_venues', views.search_venues, name='search_venues'),
    path('update_venue/<venue_id>', views.update_venue, name='update_venue'),
    path('add_events', views.add_events, name='add_events'),
    

]
   
