from django.core.management.base import BaseCommand
# from teacher.models import Teacher
# from monetary.models import Salary
from student.models import Student
from admin_home_page.models import Result
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Add Results of Students'

    def handle(self, *args, **kwargs):
        fake = Faker('en_IN')

  
        # for student in Student.objects.all().first():
        #     Result.objects.create(
        #         student_id = student.student_id,
        #         name = f"{student.first_name} {student.last_name}",
        #         marks = random.randint(200, 700),
        #         # percentage = f"{round(marks, 2)}%",
        #     )
        
        
        for student in Student.objects.all():
            marks = random.randint(200, 700)
            Result.objects.create(
                student_id = student.student_id,
                name = f"{student.first_name} {student.last_name}",
                marks = marks,
                percentage = round(marks / 7, 2),  # <-- Add this line
            )
        
        self.stdout.write(self.style.SUCCESS("Result published Successfully"))





