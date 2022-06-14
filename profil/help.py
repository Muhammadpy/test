from django.contrib import messages
from django.contrib.auth.models import User


class CheckUserData:
    
    error = None

    def security(self,request):
        adres = request.POST['adres']
        if adres.strip().startswith("<script") or adres.strip().startswith("<?"):
            messages.add_message(request,messages.WARNING, "Ism Familya va xarflardan iborat bo'lishi kerak")
            self.error = True
        return self.error


    def check_data(self,request):
        if self.security(request):
            return self.error
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if not first_name.isalpha() or  not last_name.isalpha():
            messages.add_message(request,messages.WARNING, "Ism Familya va xarflardan iborat bo'lishi kerak")
            self.error = True
            return self.error
        if (len(first_name) < 2 or len(first_name) > 20)  or \
                (len(last_name) < 2 or len(last_name) > 20):
            messages.add_message(request,messages.WARNING, "Ism Familya xato kiritildi")
            self.error = True
            return self.error
        if len(username) < 8 or  len(password) < 8:
            messages.add_message(request,messages.WARNING, "Username va parol 8 ta belgidan kam bo'lmasin")
            self.error = True
            return self.error
        if User.objects.filter(username=username).exists():    
            messages.add_message(request,messages.WARNING, "Username band")
            self.error = True
            return self.error
        if password != password_confirm:
            messages.add_message(request,messages.WARNING, "Parollar bir xil emas")
            self.error = True
        return self.error

