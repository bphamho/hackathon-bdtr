from django.shortcuts import render, redirect, get_object_or_404
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
def create_community(request):
    if request.method == 'POST':
        community_form = CreateCommunityForm(request.POST)
        if community_form.is_valid():
            new_community = community_form.save(commit=False)
            new_community.founder = request.user
            new_community.save()
            new_community.members.add(request.user)
            return redirect('community')
    else:
        community_form = CreateCommunityForm()
    return render(request, 'community_make.html', {'community_form': community_form})
    
def community_detail(request, pk):
    community = get_object_or_404(CommunityDetail, pk=pk)
    return render(request, 'community_detail.html', {'com': community})