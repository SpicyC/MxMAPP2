from django.shortcuts import render
from .models import Profile


# Create your views here.
def list_profiles(request):
  all_profiles = Profile.objects.all().order_by('name')
  return render(request, 'profiles/list_profiles.html', context={'app2' :all_profiles})