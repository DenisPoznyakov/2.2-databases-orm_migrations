# Generated by Django 4.2.15 on 2024-08-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_teacher_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='Student', to='school.teacher'),
        ),
    ]
