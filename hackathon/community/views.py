from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView
from .models import CommunityDetail

class CommunityView(ListView):
    model = CommunityDetail
    template_name = 'community.html'

class CommunityViewAdv(DetailView):
    model = CommunityDetail
    template_name = 'community_detail.html'

class MakeCommunityView(FormView):
    model = CommunityDetail
    template_name = 'make_community.html'
