from django.urls import path
from . import views

urlpatterns = [
    path('', views.SerieListView.as_view(), name="tvseries_list"),
]
