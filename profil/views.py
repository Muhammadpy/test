from django.shortcuts import render
from django.views import View
from .help import CheckUserData
# Create your views here.


class RegisterView(View,CheckUserData):
    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        if self.check_data(request):
            return render(request, "auth/register.html")
  

class LoginView(View):
    def get(self, request):
        return render(request=request, template_name="auth/login.html")
