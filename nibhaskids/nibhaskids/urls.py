from django.contrib import admin
from django.urls import path
from questions_module import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('admin_auth/',views.admin_auth,name='admin_auth'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('adminpanel/',views.adminpanel,name='adminpanel'),
    path('add_pattern/',views.add_pattern,name='add_pattern'),
    path('add_normal/',views.add_normal,name='add_normal'),
    path('logout/',views.logout,name='logout'),
    path('question/',views.question,name='question'),
    path('checktext/',views.checktext,name='checktext'),
    path('session_auth/',views.session_auth,name='session_auth'),
    path('addenroll/',views.addenroll,name='addenroll'),
    path('addclass/',views.addclass,name='addclass'),
    path('addsubject/',views.addsubject,name='addsubject'),
    path('get_enroll_data/',views.get_enroll_data,name='get_enroll_data'),
    path('get_classes_data/',views.get_classes_data,name='get_classes_data'),
    path('get_subject_data/',views.get_subject_data,name='get_subject_data'),
    path('delete_enroll/',views.delete_enroll,name='delete_enroll'),
    path('delete_classes/',views.delete_classes,name='delete_classes'),
    path('delete_subject/',views.delete_subject,name='delete_subject'),
]
