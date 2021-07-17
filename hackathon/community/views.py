from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView
from .models import CommunityDetail
from django.contrib.auth.decorators import login_required
from .forms import CreateCommunityForm
from django.http import HttpResponseRedirect

class CommunityView(ListView):
    model = CommunityDetail
    template_name = 'community.html'

class CommunityViewAdv(DetailView):
    model = CommunityDetail
    template_name = 'community_detail.html'

#class MakeCommunityView(FormView):
    #model = CommunityDetail
    #template_name = 'make_community.html'
    
@login_required
def create_community(self):
    if self.method == 'POST':
        community_form = CreateCommunityForm(self.POST)
        if community_form.is_valid():
            new_community = community_form.save(commit=False)
            new_community.founder = self.user
            new_community.members.add(self.user)
    
    return HttpResponseRedirect(self.path_info)