from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@csrf_exempt
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('OK')

    return Response({'status': 'error'})


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse('OK')


@login_required
@api_view()
def me(request):
    return Response({'user': {'username': request.user.username}})


class IndexView(TemplateView):
    template_name = "index.html"
