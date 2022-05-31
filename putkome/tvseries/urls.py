from django.urls import path
from . import views

urlpatterns = [
    path('', views.SerieListView.as_view(), name="serie_list"),
	path('<int:pk>', views.SerieDetailView.as_view(), name="serie_detail"),
	path('<int:pk>/update', views.SerieUpdateView.as_view(), name="serie_update"),
	path('<int:pk>/delete', views.SerieDeleteView.as_view(), name="serie_delete"),
	path('new/', views.SerieCreateView.as_view(), name="serie_create"),
	path('season/new', views.SeasonCreateView.as_view(), name="season_create"),
	
]
