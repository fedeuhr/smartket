from socket import fromshare
from webbrowser import get
from accounts.models import Profile
from django import forms 
from django.contrib.auth import get_user_model
User = get_user_model()

class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md', 'placeholder':'Ingrese Nombre'}), required=True)

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md', 'placeholder':'Ingrese Apellido'}),required=True)

    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md', 'placeholder':'Ingrese dirección de Email'}),required=True)

    picture = forms.ImageField(label='Profile Picture', required=False, widget=forms.FileInput(attrs={'class':'appearance-none bg-gray-200 text-gray-900 px-2 py-1 shadow-sm border border-gray-400 rounded-md'}))

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture', 'email')

