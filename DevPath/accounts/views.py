from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


class CustomLogoutView(LogoutView):
    """Custom logout view with proper CSRF handling"""
    template_name = 'registration/logged_out.html'
    next_page = 'home'
    
    def dispatch(self, request, *args, **kwargs):
        # Handle both GET and POST for logout
        if request.method == 'GET':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
