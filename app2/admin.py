from django.contrib import admin

# Register your models here.

from .models import Profile
#from .models import Bio

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','citystate')
admin.site.register(Profile)


#class BioAdmin(admin.ModelAdmin):
    #list_display= ('interests', 'about_me')