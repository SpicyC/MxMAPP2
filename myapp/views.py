from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import profileForm

# Create your views here.

def index(request):
  all_profiles = Profile.objects.all().order_by('name')
  
  return render(request, 'profiles/list_profiles.html',
  {"profiles": all_profiles})

def add_profiles(request):
    if request.method == 'GET':
        form = profileForm()
    else:
        form = profileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles')

    return render(request, "profiles/add_profiles.html", {"form": form})

def delete_profiles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        profile.delete()
    
    return render(request,
    "profiles/delete_profiles.html",
    {"profile":profile})
    
def profiles_details(request, pk):
  profile = get_object_or_404(Profile, pk=pk)
  return render(request, "profiles/profiles_details.html", {"profile": profile})



def edit_profiles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'GET':
        form = profileForm(instance=profile)
    else:
        form = profileForm(data=request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect(to='list_profiles.html')

    return render(request, "profiles/edit_profiles.html", {
        "form": form, "profile": profile})


