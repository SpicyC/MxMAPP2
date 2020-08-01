from django import forms



from .models import Profile 
#from .Models import bio

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'citystate',
            'email',  
        ]