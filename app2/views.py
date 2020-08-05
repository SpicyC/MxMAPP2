from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile, Bio
from .forms import ProfileForm


# Create your views here.
def list_profiles(request):
  all_profiles = Profile.objects.all().order_by('name') 
  
  return render(request, 'profiles/list_profiles.html', context={'app2':all_profiles})


def profile_details(request, pk):
  bio = get_object_or_404(Bio, pk=pk)
  return render(request, 'profiles/profile_details.html',{'bio': bio})

  return render(request, 
  'profiles/profile_details.html',{'bio': bio})


def update_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'GET':
        form = ProfileForm(instance=Profile)
    else:
        form= ProfileForm(data=request.POST, instance=Profile)
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "profiles/update_profile.html",{"form": form,
    "profile": profile})



def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect(to='list_profiles')

    return render(request, "profiles/delete_profile.html",              {"profile": profile})


def add_profile(request):
    if request.method == 'GET':
       form = ProfileForm()
    else:
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "profiles/add_profile.html", {"form": form})

    
