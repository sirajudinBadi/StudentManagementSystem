from django.core.management.base import BaseCommand
from teacher.models import Teacher
from monetary.models import Salary
from faker import Faker
import random
from datetime import datetime, date


from django.core.management.base import BaseCommand
from student.models import Student
from monetary.models import Fees
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fee data for students'

    def handle(self, *args, **kwargs):
        fake = Faker('en_IN')

        for teacher in Teacher.objects.all():
          if teacher.teacher_experience in ["3", "4", "5"]:
            Salary.objects.create(
              staff_id = teacher.teacher_id,
              name = f"{teacher.teacher_first_name} {teacher.teacher_last_name}",
              gender = teacher.gender,
              join_date = teacher.teacher_join_date,
              salary_amount = "50000",
              status = True,
            )
          elif teacher.teacher_experience in ["6", "7", "8"]:
            Salary.objects.create(
              staff_id = teacher.teacher_id,
              name = f"{teacher.teacher_first_name} {teacher.teacher_last_name}",
              gender = teacher.gender,
              join_date = teacher.teacher_join_date,
              salary_amount = "80000",
              status = True,
            )
          elif teacher.teacher_experience in ["9", "10", "11", "12"]:
            Salary.objects.create(
              staff_id = teacher.teacher_id,
              name = f"{teacher.teacher_first_name} {teacher.teacher_last_name}",
              gender = teacher.gender,
              join_date = teacher.teacher_join_date,
              salary_amount = "100000",
              status = True,
            )
        
        self.stdout.write(self.style.SUCCESS("Salary generated for all Teachers."))





