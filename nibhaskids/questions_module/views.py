from django.shortcuts import render,redirect
from .forms import Admin_Form,Normal_question_form,Pattern_question_form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.core.cache import cache
import os
from .service import random_hash,save_file,admin_authentication
from django.contrib.auth import authenticate,login

# Create your views here.


def home(request):
    print(random_hash()+str(cache.get('image_number')))
    print(random_hash()+str(cache.get('image_number')))
    print(random_hash()+str(cache.get('image_number')))
    cache.set('image_number',(cache.get('image_number'))+1,timeout=None)
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
            if admin_authentication(username,password):
                print('success')
                return render(request,'adminpanel.html')

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def admin_login(request):
    return render(request,'admin_login.html')


def adminpanel(request):
    return render(request,'adminpanel.html')


@csrf_exempt
def add_pattern(request):
    if request.method == 'POST':
        try:
            question_name = request.POST.get('question_name')
            question = request.POST.get('question')
            age = request.POST.get('age')
            question_image=request.FILES['question_image']
            a=request.FILES['a']
            b=request.FILES['b']
            c=request.FILES['c']
            d=request.FILES['d']
            answer=request.POST.get('answer')
            if question_image and a and b and c and d and answer :
                image_tuple=(
                (question_image,cache.get('question_path')+random_hash()+str(cache.get('image_number'))+'.jpg'),
                (a,cache.get('option_path')+random_hash()+str(cache.get('image_number'))+'.jpg'),
                (b,cache.get('option_path')+random_hash()+str(cache.get('image_number'))+'.jpg'),
                (c,cache.get('option_path')+random_hash()+str(cache.get('image_number'))+'.jpg'),
                (d,cache.get('option_path')+random_hash()+str(cache.get('image_number'))+'.jpg'),
                )
                cache.set('image_number',(cache.get('image_number'))+1,timeout=None)
                for i,j in image_tuple:
                #upload_path=os.path.join(j,k)
                    save_file(j,i)
            
                p_form=Pattern_question_form(data={
                    'question_name':question_name,
                    'question':question,
                    'question_image':image_tuple[0][1],
                    'age':age,
                    'a':image_tuple[1][1],
                    'b':image_tuple[2][1],
                    'c':image_tuple[3][1],
                    'd':image_tuple[4][1],
                    'answer':answer}
                )   

                if p_form.is_valid():
                    p_form.save()
                    return JsonResponse({'success': 'Image uploaded successfully!'}, status=200)
                else:
                    return JsonResponse({'error': 'failed to insert'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)


@csrf_exempt
def add_normal(request):
    if request.method == 'POST':
        try:
            question_name = request.POST.get('n_question_name')
            question = request.POST.get('n_question')
            age = request.POST.get('n_age')
            a = request.POST.get('n_a')
            b = request.POST.get('n_b')
            c = request.POST.get('n_c')
            d = request.POST.get('n_d')
            answer = request.POST.get('n_answer')

            n_form=Normal_question_form(data={
                'question_name':question_name,
                'question':question,
                'age':age,
                'a':a,
                'b':b,
                'c':c,
                'd':d,
                'answer':answer}
            )   
                 
            if n_form.is_valid():
                n_form.save()
                return JsonResponse({'success':'normal question added successfully!'},status=200)
            else:
                return JsonResponse({'error': 'failed to insert'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)


@csrf_exempt
def sendimage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        image.append(request.FILES['imagefile1'])
        image.append(request.FILES['imagefile2'])
        image.append(request.FILES['imagefile3'])
        question_dir = 'media/questions/question_images/'
        options_dir = 'media/questions/options/'
        answers_dir = 'media/questions/answers/'
        filename = 'uploaded_image.jpg'  # You can customize the filename as needed
        print(cache.get('question_path'))
        print(cache.get('option_path'))
        print(cache.get('answer_path'))
        print(cache.get('image_number'))
        cache.set('image_number',(cache.get('image_number'))+1,timeout=None)
        print(cache.get('image_number'))


        #for i in image:
           # question_path = os.path.join('media/questions/', filename)
        # with open(upload_path,'wb') as f:
            #    for chunk in image.chunks():
            #       f.write(chunk)


        return JsonResponse({'success': 'Image uploaded successfully!'}, status=200)
    else:
        # Return a JSON response indicating bad request
        return JsonResponse({'error': 'Bad request'}, status=400)


