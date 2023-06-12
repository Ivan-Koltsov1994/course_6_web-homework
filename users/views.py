from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import CustomUserChangeForm, UserRegisterForm
from users.models import User


class ProfileUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('catalog:product_list')


    def get_object(self, queryset=None):
        return self.request.user

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:product_list')