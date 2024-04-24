from django.shortcuts import render
from .forms import Admin_Form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request,'index.html')

@csrf_exempt
def admin_auth(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            username=data.get('username')
            password=data.get('password')
            form=Admin_Form(data={'username':username,'password':password})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        if form.is_valid():
            #do authentication
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            # Form data is invalid, return errors
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def admin_login(request):
    return render(request,'admin_login.html')