from django.contrib import admin
from .models import UserLibrary,User,Profile

admin.site.register(User)
admin.site.register(UserLibrary)
admin.site.register(Profile)
