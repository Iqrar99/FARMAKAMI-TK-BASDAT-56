from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def user_login(request):

    response = {}

    form = LoginForm(request.POST or None)
    if (request.method == 'POST' and form.is_valid()):
        response['email'] = request.POST['email']
        response['password'] = request.POST['password']

        if verified(response):
            # TODO
            pass

    response['form'] = form

    return render(request, 'login.html', context = response)