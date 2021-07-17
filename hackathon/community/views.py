from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import CommunityDetail

class CommunityView(ListView):
    model = CommunityDetail
    template_name = 'community.html'
