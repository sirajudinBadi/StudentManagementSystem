from django.core.management.base import BaseCommand
from student.models import Student
from monetary.models import Fees
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fee data for students'

    def handle(self, *args, **kwargs):
        fake = Faker('en_IN')

        for student in Student.objects.all():
          
          Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Transport Fees",
              fees_amount = "10000",
              paid_date = student.joining_date,
              paid_status = True,
            )

          if student.student_class in ["LKG", "UKG", "1", "2", "3", "4"]:
            Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Miscellaneous Fees",
              fees_amount = "500",
              paid_date = student.joining_date,
              paid_status = True,
            )
            
            Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Academic Fees",
              fees_amount = "40000",
              paid_date = student.joining_date,
              paid_status = True,
            )

          elif student.student_class in ["5", "6", "7", "8"]:
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Class Test Fees",
              fees_amount = "1000",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Academic Fees",
              fees_amount = "60000",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Exam Fees",
              fees_amount = "1500",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Miscellaneous Fees",
              fees_amount = "1000",
              paid_date = student.joining_date,
              paid_status = True,
            )
          else:
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Class Test Fees",
              fees_amount = "1000",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Academic Fees",
              fees_amount = "80000",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Miscellaneous Fees",
              fees_amount = "500",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Exam Fees",
              fees_amount = "1500",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Hostel Fees",
              fees_amount = "20000",
              paid_date = student.joining_date,
              paid_status = True,
            )
             Fees.objects.create(
              student_id = student.student_id,
              student_name = f"{student.first_name} {student.last_name}",
              gender = student.gender,
              fees_type = "Mess Fees",
              fees_amount = "300",
              paid_date = student.joining_date,
              paid_status = True,
            )
             
        # fake = Faker('en_IN')

        # for student in Student.objects.all():
        #     student_class = str(student.student_class)

        #     if student_class in ["LKG", "UKG", "1", "2", "3", "4"]:
        #         fees_type = "Transport Fees"
        #         fees_amount = 10000
        #     elif student_class in ["5", "6", "7", "8"]:
        #         fees_type = "Class Test Fees"
        #         fees_amount = 1000
        #     else:
        #         fees_type = "Annual Fees"
        #         fees_amount = 15000

        #     Fees.objects.create(
        #         student_id = student.student_id,
        #         student_name = f"{student.first_name} {student.last_name}",
        #         gender = student.gender,
        #         fees_type = fees_type,
        #         fees_amount = fees_amount,
        #         paid_date = fake.date_between(start_date=student.joining_date, end_date='today'),
        #         paid_status = True,
        #     )

        self.stdout.write(self.style.SUCCESS("Fees generated for all students."))

