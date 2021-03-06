from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from .forms import ProfileForm


# Create your views here.
def list_profiles(request):
  all_profiles = Profile.objects.all().order_by('name') 
  
  return render(request, 'profiles/list_profiles.html', context={'app2':all_profiles})


#def list_bio(request):
    #all_bios = Bio.objects.all()
   # .order_by():  