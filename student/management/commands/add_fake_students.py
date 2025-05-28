from django.core.management.base import BaseCommand
from student.models import Student, Parent, Skills
from faker import Faker
import random
from datetime import datetime, date

fake = Faker('en_IN')

class Command(BaseCommand):
    help = "Generate fake student data"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of students to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            
            # start_date = date(2015, 1, 1)
            # end_date = date.today()
            
            gender = random.choice(['Male', 'Female', 'Other'])
            dob=fake.date_between(start_date=date(2009, 1, 1), end_date=date(2019, 10, 12))
            join_date=fake.date_between(start_date=date(2015, 1, 1), end_date=date.today())

            skills = Skills.objects.create(
                communication_skill = random.randint(75, 100),
                problem_solving = random.randint(75, 100),
                technical_skill = random.randint(75, 100),
                discipline = random.randint(75, 100),
            )

            parent = Parent.objects.create(
              father_name=fake.name_male(),
              father_occupation=fake.job(),
              father_mobile=fake.msisdn()[:10],
              father_email=fake.unique.email(),
              mother_name=fake.name_female(),
              mother_occupation=fake.job(),
              mother_mobile=fake.msisdn()[:10],
              mother_email=fake.unique.email(),
              present_address=fake.address(),
              permanent_address=fake.address(),
            )

            Student.objects.create(
              first_name=fake.first_name(),
              last_name=fake.last_name(),
              student_email=fake.unique.email(),
              student_id=f"STUD{1001 + i}",
              gender=gender,
              student_dob= str(dob),#fake.date_between(start_date='-16y', end_date='-6y'),
              student_class=random.choice(["LKG", "UKG", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]),
              joining_date=str(join_date),#fake.date_between(start_date='2015-01-01', end_date='today'),
              mobile_number=fake.msisdn()[:10],
              admission_number=1000 + i,
              student_section=random.choice(['A', 'B', 'C']),
              religion=random.choice(['Muslim', 'Hindu', 'Christian']),
              parent=parent,
              skills = skills,
            )

            

            # # student = Student.objects.create(
            #     first_name = fake.first_name(),
            #     last_name = fake.last_name(),
            #     email = fake.unique.email(),
            #     student_id = f"STUD{i+1:04d}",
            #     gender = gender,
            #     student_dob = dob,
            #     religion = random.choice(["Muslim", "Hindu", "Christian", "Sikh"]),
            #     student_class = random.choice(["LKG", "UKG", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]),
            #     joining_date = join_date,
            #     mobile_number = fake.msisdn()[0:10],
            #     admission_number = i + 1,
            #     student_section = random.choice(["A", "B", "C", "D"]),
            #     parent.father_name = fake.name_male(),
            #     parent.father_occupation = fake.job(),
            #     parent.father_mobile = fake.msisdn()[0:10],
            #     parent.father_email = fake.unique.email(),
            #     parent.mother_name = fake.name_female(),
            #     parent.mother_occupation = fake.job(),
            #     parent.mother_mobile = fake.msisdn()[0:10],
            #     parent.mother_email = fake.unique.email(),
            #     parent.present_address = fake.address(),
            #     parent.permanent_address = fake.address()
            # )
        self.stdout.write(self.style.SUCCESS(f"Successfully added {total} students."))
