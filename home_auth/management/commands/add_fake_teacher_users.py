from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from teacher.models import Teacher
from home_auth.models import CustomUser

class Command(BaseCommand):
    help = 'Add fake teacher users'

    def handle(self, *args, **kwargs):
        fake = Faker()
        User = get_user_model()

        for teacher in Teacher.objects.all():  # generate 10 fake teachers
            first_name = teacher.teacher_first_name
            last_name = teacher.teacher_last_name
            email = teacher.teacher_email
            password = "preschool@123"
            # confirm_password = password

            if not User.objects.filter(email=email).exists():
                user = CustomUser.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    # confirm_password=password,
                    role='Teacher'
                )
        
        self.stdout.write(self.style.SUCCESS("Teacher Users Created Successfully"))
