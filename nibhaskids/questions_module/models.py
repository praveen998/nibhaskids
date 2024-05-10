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
        enroll_type=models.CharField(max_length=100)
        question_name=models.CharField(max_length=100)
        question=models.CharField(max_length=500)
        question_image=models.CharField(max_length=100)
        a=models.CharField(max_length=100)
        b=models.CharField(max_length=100)
        c=models.CharField(max_length=100)
        d=models.CharField(max_length=100)
        answer=models.CharField(max_length=100)

        class meta:
            db_table= 'Pattern_question'

class Normal_question(models.Model):
    qid=models.AutoField(primary_key=True)
    enroll_type=models.CharField(max_length=100)
    question_name=models.CharField(max_length=100)
    question=models.CharField(max_length=500)
    a=models.CharField(max_length=100)
    b=models.CharField(max_length=100)
    c=models.CharField(max_length=100)
    d=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

    class meta:
        db_table= 'Normal_question'


class Session_table(models.Model):
    sid=models.AutoField(primary_key=True)
    session_id=models.CharField(max_length=100)
    user=models.CharField(max_length=50)
    user_id=models.IntegerField()

    class meta:
        db_table='Session_table'

class Enrolls(models.Model):
    enroll_id=models.AutoField(primary_key=True)
    enroll_types=models.CharField(max_length=100)

class Classes(models.Model):
    class_id=models.AutoField(primary_key=True)
    class_types=models.CharField(max_length=100)
    enroll_id=models.ForeignKey(Enrolls,on_delete=models.CASCADE)

class Subjects(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_types=models.CharField(max_length=100)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
 
 



    


