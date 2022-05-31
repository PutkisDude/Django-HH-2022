from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from tvseries.models import Serie, Episode, Season
from django.db.models import Count

class SerieListView(ListView):
	paginate_by = 5
	model = Serie

class SerieDetailView(DetailView):
	model = Serie

	def get_context_data(self, **kwargs):
		context = super(SerieDetailView, self).get_context_data(**kwargs)
		context['seasons'] = Season.objects.all().filter(serie=self.kwargs['pk']).count()
		return context

class SerieCreateView(LoginRequiredMixin, CreateView):
	model = Serie
	fields = ["name", "description"]
	login_url = "login"
	success_url = reverse_lazy('serie_list')
    
class SerieUpdateView(LoginRequiredMixin, UpdateView):
	model = Serie
	fields = ["name", "description"]
	login_url = "login"

class SerieDeleteView(LoginRequiredMixin, DeleteView):
	model = Serie
	success_url = reverse_lazy("serie_list")
	login_url = "login"



class SeasonCreateView(LoginRequiredMixin, CreateView):
	model = Season
	fields = ["serie", "season_number"]
	login_url = "login"

class SeasonDetailView(LoginRequiredMixin, DetailView):
	model = Season
	login_url = "login"


class EpisodeCreateView(LoginRequiredMixin, CreateView):
	model = Episode
	fields = ["season", "episode_number"]
	login_url = "login"
	success_url = reverse_lazy("episode_create")
