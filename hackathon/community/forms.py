from .models import CommunityDetail
from django import forms

class CreateCommunityForm(forms.ModelForm):
    class Meta:
        model = CommunityDetail
        fields = ['name', 'description', 'image']