import json
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todo.auth_.models import MyUser


@csrf_exempt
def login(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return JsonResponse({'message': 'You are successfully logged in!'}, status=200)

    else:
        return JsonResponse({'message': 'User with this login/password is not found.'}, status=200)


@csrf_exempt
def logout(request):
    user = auth.logout(request)
    return JsonResponse({'message': 'You are logged out.'}, status=200)


@csrf_exempt
def register(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    email = body.get('email')
    password = body.get('password')

    user = MyUser.objects.create_user(username=username, email=email)
    user.set_password(password)
    user.save()
    return JsonResponse({'message': f'The user with username: {user.username} and email: {user.email} created'}, status=200)