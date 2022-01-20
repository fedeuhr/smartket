from cProfile import Profile
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from accounts.forms import EditProfileForm
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()

class UserProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        context={
            'user':user,
            'profile':profile
        }
        return render(request, 'users/detail.html', context)

@login_required
def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)
    user_basic_info = User.objects.get(id=user)

    if request.method == 'POST':
        form=EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.email = form.cleaned_data.get('email')
            
            profile.picture = form.cleaned_data.get('picture')

            profile.save()
            user_basic_info.save()
            
            return redirect('users:profile', username=request.user.username)

    else:
        form = EditProfileForm(instance=profile)

    context={
        'form':form,
    }

    return render(request, 'users/edit.html', context)
