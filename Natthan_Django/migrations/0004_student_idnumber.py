# Generated by Django 4.1.7 on 2023-03-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Natthan_Django', '0003_student_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='idnumber',
            field=models.IntegerField(default=1),
        ),
    ]