from django.contrib import admin
from .models import Admin,Pattern_question,Normal_question,Session_table
from .models import Enrolls,Classes,Subjects
# Register your models here.

admin.site.register(Admin)
admin.site.register(Pattern_question)
admin.site.register(Normal_question)
admin.site.register(Session_table)

admin.site.register(Enrolls)
admin.site.register(Classes)
admin.site.register(Subjects)

