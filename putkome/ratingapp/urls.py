from django.urls import path
from .views import RatingCreateView, RatingListView, RatingDeleteView, RatingUpdateView

urlpatterns = [
	path('', RatingListView.as_view(), name="rating_list"),
	path('<int:pk>', RatingCreateView.as_view(), name="rating"),
	path('<int:pk>/delete', RatingDeleteView.as_view(), name="rating_delete"),
	path('<int:pk>/update', RatingUpdateView.as_view(), name="rating_update"), 
]
