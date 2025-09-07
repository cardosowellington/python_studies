from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib import messages

def register(request):
  template_name = 'accounts/register.html'
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Usuário cadastrado com sucesso!')
      return redirect(settings.LOGIN_URL)
    else:
      print(form.errors)
      messages.error(request, 'Erro ao cadastrar usuário!')
  else:
    form = UserCreationForm()
  context = {
    'form': form
  }
  return render(request, template_name, context)
