from django.shortcuts import render
# Create your views here.


def user_profile(request):
    context = {}
    return render(request, 'user_profile.html', context)
