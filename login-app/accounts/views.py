from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserUpdateForm
from .forms import CustomUserCreationForm 
from django.contrib.auth.mixins import UserPassesTestMixin 

# Devuelve el modelo de usuario requerido
User = get_user_model()

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser
    
class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm   # Cambiamos a la clase de formulario estándar de Django
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        # Llamamos al método form_valid() de la superclase para guardar el usuario
        response = super().form_valid(form)
        # Autenticamos al usuario y lo redirigimos al éxito.
        username = form.cleaned_data.get("username")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_pw)
        login(self.request, user)
        return response
    
    @login_required  # Asegura que el usuario esté autenticado
    def get(self, request, *args, **kwargs):
        return redirect(self.success_url)

class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/edit_user.html'
    # se ejecuta si la actualizacion es exitosa
    def get_success_url(self):
        # toma el argumento pk definido en la ruta y redirige a la pagina de detalles
        # del usuario usando el mismo argumento => user_detail/<int:pk>
        return reverse('user_detail', kwargs={'pk': self.kwargs['pk']})
    
class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password_change.html'
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/user_detail.html'
class UserDelete(OnlyYouMixin, DeleteView):
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = reverse_lazy('login')