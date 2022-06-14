from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin,View):
    def get(self, request):     
        return render(request=request, template_name="index.html")


