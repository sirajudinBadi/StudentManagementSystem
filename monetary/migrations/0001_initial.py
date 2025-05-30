# Generated by Django 5.1.1 on 2025-04-17 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=50)),
                ('student_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50)),
                ('fees_type', models.CharField(choices=[('Select Type', 'Select Type'), ('Class Test Fee', 'Class Test Fees'), ('Exam Fees', 'Exam Fees'), ('Hostel Fees', 'Hostel Fees'), ('Transport Fees', 'Transport Fees'), ('Mess Fees', 'Mess Fees'), ('Miscellaneous Fees', 'Miscellaneous Fees')], max_length=50)),
                ('fees_amount', models.CharField(max_length=100)),
                ('paid_date', models.DateField(auto_now_add=True)),
                ('paid_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('join_date', models.DateField()),
                ('salary_amount', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
