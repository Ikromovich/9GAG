from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import User



class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Royxatdan o'tish !")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': RegistrationForm()
        })


    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, ("Siz muvaffaqiyatli ro'yxatdan o'tdingiz !! "))
            return redirect('main:index')


        return render(request, 'layouts/form.html', {
            'form': form
        })




class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = ("Tizimga kirish")

    def get(self, request):
        return render(request, "layouts/form.html", {
            "form": LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if not user is None:
                login(request, user)
                messages.success(request, ("Xush kelibsiz, {}!".format(user.username)))

                return redirect("main:index")

            form.add_error("password", ("Login va/yoki parol notoʻgʻri."))

        return render(request, "layouts/form.html", {
            "form": form
        })


@login_required
def clinet_logout(request):
    messages.success(request, "Xayr {}!".format(request.user.username))
    logout(request)

    return redirect("main:index")


class ClientProfile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', "last_name", 'username', 'email','photo']
    template_name = "layouts/form.html"
    success_url = reverse_lazy('client:profile')

    def setup(self,request,*args,**kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Profile")
        request.button_title = _("Saqlash")

    def get_object(self, queryset=None):
        return self.request.user