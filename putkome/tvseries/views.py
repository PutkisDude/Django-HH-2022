from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from tvseries.models import Serie

class SerieListView(ListView):
	paginate = 10
	model = Serie
