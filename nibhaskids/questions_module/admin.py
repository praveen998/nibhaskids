from django.contrib import admin
from .models import Admin,Pattern_question,Normal_question
# Register your models here.
admin.site.register(Admin)
admin.site.register(Pattern_question)
admin.site.register(Normal_question)

