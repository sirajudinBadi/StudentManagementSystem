# Generated by Django 5.1.1 on 2025-04-18 10:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_solving', models.IntegerField(default=75, help_text='Enter Value between 60 to 100', validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(100)])),
                ('technical_skill', models.IntegerField(default=75, help_text='Enter Value between 60 to 100', validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(100)])),
                ('discipline', models.IntegerField(default=75, help_text='Enter Value between 60 to 100', validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(100)])),
                ('communication_skill', models.IntegerField(default=75, help_text='Enter Value between 60 to 100', validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='skills',
            field=models.OneToOneField(default=75, on_delete=django.db.models.deletion.CASCADE, to='student.skills'),
            preserve_default=False,
        ),
    ]
