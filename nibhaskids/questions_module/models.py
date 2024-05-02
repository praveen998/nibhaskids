from django.db import models

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class meta:
        db_table= 'Admin'


class Pattern_question(models.Model):
        qid=models.AutoField(primary_key=True)
        question_name=models.CharField(max_length=100)
        question=models.CharField(max_length=500)
        question_image=models.CharField(max_length=100)
        a=models.CharField(max_length=100)
        b=models.CharField(max_length=100)
        c=models.CharField(max_length=100)
        d=models.CharField(max_length=100)
        answer=models.CharField(max_length=100)
        age=models.IntegerField() 

        class meta:
            db_table= 'Pattern_question'

class Normal_question(models.Model):
    qid=models.AutoField(primary_key=True)
    question_name=models.CharField(max_length=100)
    question=models.CharField(max_length=500)
    a=models.CharField(max_length=100)
    b=models.CharField(max_length=100)
    c=models.CharField(max_length=100)
    d=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    age=models.IntegerField() 

    class meta:
        db_table= 'Normal_question'
        
        