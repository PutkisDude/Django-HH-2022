from django.shortcuts import render
from .models import Rating
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rating
from tvseries.models import Episode

class RatingCreateView(LoginRequiredMixin, CreateView):
	model = Rating
	fields = ["rating"]
	
	def form_valid(self, form):
		pk = self.kwargs['pk']
		form.instance.episode = Episode.objects.get(pk=pk)
		form.instance.user = self.request.user
		return super().form_valid(form)		

class RatingListView(ListView):

	def get_queryset(self):
		return Rating.objects.filter(user=self.request.user)


class RatingDeleteView(LoginRequiredMixin, DeleteView):
	model = Rating
	success_url = reverse_lazy('rating_list')

class RatingUpdateView(LoginRequiredMixin, UpdateView):
	model = Rating
	fields = ["rating"]
	success_url = reverse_lazy('rating_list')
