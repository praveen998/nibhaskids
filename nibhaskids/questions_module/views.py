from django.shortcuts import render,redirect
from .forms import Admin_Form,Normal_question_form,Pattern_question_form
from .forms import Enrolls_form,Classes_form,Subjects_form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.core.cache import cache
import os
from .service import random_hash,save_file,admin_authentication,get_client_ip
from django.contrib.auth import authenticate,login
from .models import Session_table,Enrolls,Classes,Subjects



# Create your views here.
question_list=[100,101,102,103,104,105]
q_index=-1



#root page return index page ur("/")------------------------------------------------------------------
def home(request):
    cache.set('image_number',(cache.get('image_number'))+1,timeout=None)
    return render(request,'index.html')



def question(request):
    return JsonResponse({'success': 'successfully login!','data':question_list}, status=200)

#checking async api connection with front end--------------------------------------------------------
@csrf_exempt
def checktext(request):
    if request.method == 'POST':
        inputs=request.POST.get('q')
        if inputs == 'praveen':
            return  JsonResponse({'success': 'valid name'}, status=200)
        else:
            return JsonResponse({'success': 'invalid name'}, status=200)


#add enroll table data----------------------------------------------------------------------------
@csrf_exempt
def addenroll(request):
    if request.method == "POST":
        data=json.loads(request.body)
        print(data.get('enroll'))
        try:
            Enrolls.objects.create(enroll_types=data.get('enroll'))
            return JsonResponse({'success':'Enroll added successfully!'},status=200)   
        except Exception as e:
            return JsonResponse({'success':str(e)},status=200)
    else:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400) 

#add classes table data--------------------------------------------------------------------------
@csrf_exempt
def addclass(request):
    if request.method == "POST":
        try:
            data=json.loads(request.body)
            enroll=Enrolls.objects.filter(enroll_types=data.get('enroll'))
            if enroll.count()==1:
               for obj in enroll:
                    Classes_instance=Classes.objects.create(
                        class_types=data.get('classes'),
                        enroll_id=obj)
                    return JsonResponse({'success':"class added"},status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        

#add subject table data---------------------------------------------------------------------------
@csrf_exempt
def addsubject(request):
    eid=None
    cid=None
    if request.method == "POST":
        try:
            data=json.loads(request.body)
            enroll=Enrolls.objects.filter(enroll_types=data.get('enroll'))
            for obj1 in enroll:
                eid=obj1
            classes=Classes.objects.filter(class_types=data.get('classes')).filter(enroll_id_id=eid)
            for obj2 in classes:
                cid=obj2
            print(f"subject:{data.get('subject')}")
            print(f"enroll_id:{eid.enroll_id}")
            print(f"class_id:{cid.class_id}")
            Subjects.objects.create(subject_types=data.get('subject'),enroll_id=eid,class_id=cid)
            return JsonResponse({'success': 'subject added'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)


#checking session id-----------------------------------------------------------------------------
@csrf_exempt
def session_auth(request):
    if request.method == 'POST':
        jwt=request.headers.get('token')
        print(jwt)
        if  jwt:
            token=jwt.strip()
            print("token:",token)
            return JsonResponse({'message':'token printed'})
        else:
            return JsonResponse({'error':'header is missing'},status=400)
    else:
       return JsonResponse({'error':'method not allowed'},status=405)


#admin login api----------------------------------------------------------------------------------------
@csrf_exempt
def admin_auth(request):
    
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            username=data.get('username')
            password=data.get('password')

            #username=request.POST.get('username')
            #password=request.POST.get('password')
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        if admin_authentication(username,password):
            ip=get_client_ip(request)
            cache.set(ip,username,timeout=None)
            print(ip)
            response=JsonResponse({'success': 'successfully login!','name':'praveen'}, status=200)
            return response
        else:
            return JsonResponse({'error': 'invalid username and password'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


#admin login page return api---------------------------------------------------------------
def admin_login(request):
    return render(request,'admin_login.html')



def adminpanel(request):
    return render(request,'adminpanel.html')


#add pattern question form api-----------------------------------------------------------------
@csrf_exempt
def add_pattern(request):
    if request.method == 'POST':
        try:
            enroll=request.POST.get('enroll')
            classes=request.POST.get('classes')
            subject=request.POST.get('subject')
            enroll_type=enroll+'-'+classes+'-'+subject
            question_name = request.POST.get('question_name')
            question = request.POST.get('question')
            answer=request.POST.get('answer')
            question_image=request.FILES['question_image']
            a=request.FILES['a']
            b=request.FILES['b']
            c=request.FILES['c']
            d=request.FILES['d']
         
            if question_image and a and b and c and d :
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
                    'enroll_type':enroll_type,
                    'question_name':question_name,
                    'question':question,
                    'question_image':image_tuple[0][1],
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


#add normal question form api---------------------------------------------------------------
@csrf_exempt
def add_normal(request):
    ip=get_client_ip(request)
    if request.method == 'POST':
        try:
            enroll=request.POST.get('n_enroll')
            classes=request.POST.get('n_classes')
            subject=request.POST.get('n_subject')
            enroll_type=str(enroll)+'-'+str(classes)+'-'+str(subject)
            question_name = request.POST.get('n_question_name')
            question = request.POST.get('n_question')
            a = request.POST.get('n_a')
            b = request.POST.get('n_b')
            c = request.POST.get('n_c')
            d = request.POST.get('n_d')
            answer = request.POST.get('n_answer')

            n_form=Normal_question_form(data={
                'enroll_type':enroll_type,
                'question_name':question_name,
                'question':question,
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


#logout session api---------------------------------------------------------------------
def logout(request):
    if request.method == 'GET':
        return JsonResponse({'success':'Log out!'},status=200)
    else:
        return JsonResponse({'error': 'Bad request'}, status=405)


#api for sending all enroll,classes,subject----------------------------------------------
def get_enroll_data(request):
    if request.method == 'GET':

        return JsonResponse({'success':'Log out!'},status=200)
    else:
        return JsonResponse({'error': 'Bad request'}, status=405)

@csrf_exempt
def get_classes_data(request):
    if request.method == 'GET':
        
        return JsonResponse({'success':'Log out!'},status=200)
    else:
        return JsonResponse({'error': 'Bad request'}, status=405)

@csrf_exempt
def get_subject_data(request):
    if request.method == 'GET':
        
        return JsonResponse({'success':'Log out!'},status=200)
    else:
        return JsonResponse({'error': 'Bad request'}, status=405)




