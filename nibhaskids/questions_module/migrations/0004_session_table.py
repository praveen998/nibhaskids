# Generated by Django 5.0.4 on 2024-05-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_module', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session_table',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('session_id', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
