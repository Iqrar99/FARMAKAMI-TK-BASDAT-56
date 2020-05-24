from django.shortcuts import render, redirect

def user_logout(request):
    """
    function untuk user logout.
    """
    if 'email' not in request.session:
        return redirect('/')

    if (request.method == 'POST'):
        request.session.flush()
        return redirect('/login/')

    return render(request, 'logout.html')

def back_home(request):

    return redirect(f'/navigate/{request.session["role"]}/')
