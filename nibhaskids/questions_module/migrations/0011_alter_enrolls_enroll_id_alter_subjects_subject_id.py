# Generated by Django 5.0.4 on 2024-05-13 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_module', '0010_alter_subjects_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolls',
            name='enroll_id',
            field=models.AutoField(default=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='subject_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]