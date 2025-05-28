from django.core.management.base import BaseCommand
from teacher.models import Teacher, Education, Skills, Responsibility
from faker import Faker
import random
from datetime import datetime, date

fake = Faker('en_IN')

class Command(BaseCommand):
    help = "Generate fake student data"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of teachers to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            
            
            # start_date = date(2015, 1, 1)
            # end_date = date.today()
            def generate_school_name():
              prefixes = ["St.", "Mount", "Greenwood", "National", "Springfield", "Bright Future", "Global", "Sunrise"]
              suffixes = ["Public School", "High School", "Academy", "School", "Convent", "Vidyalaya", "International School"]
              return f"{random.choice(prefixes)} {random.choice(suffixes)}"
            
            def generate_college_name():
              prefixes = ["National", "Global", "St.", "Shri", "Government", "Institute of", "Indian", "Dr.", "Techno"]
              subjects = ["Engineering", "Technology", "Science", "Arts", "Management", "Medical", "Pharmacy", "Commerce"]
              suffixes = ["College", "University", "Institute", "Academy", "Campus"]

              if "Institute" in prefixes or "Institute of" in prefixes:
                  return f"{random.choice(prefixes)} {random.choice(subjects)}"
              else:
                  return f"{random.choice(prefixes)} {random.choice(subjects)} {random.choice(suffixes)}"
              

            def generate_random_college_name():
              prefix = random.choice([
                  "National", "Global", "Indian", "Shri", "St.", "Dr.", "Mahatma", "Rajiv Gandhi", 
                  "Subhash Chandra Bose", "Vivekananda", "Saraswati", "Kalinga"
              ])
              subject = random.choice([
                  "Engineering", "Technology", "Medical Sciences", "Management", "Arts", 
                  "Commerce", "Design", "Law", "Pharmaceutical Sciences", "Education", "Computing"
              ])
              suffix = random.choice([
                  "Institute", "College", "University", "Academy", "School", "Center", 
                  "Faculty", "Campus", "College of Advanced Studies"
              ])

              if "Institute" in suffix or "School" in suffix:
                  return f"{prefix} {suffix} of {subject}"
              elif "College" in suffix:
                  return f"{prefix} {suffix} of {subject}"
              else:
                  return f"{prefix} {subject} {suffix}"

            gender = random.choice(['Male', 'Female', 'Other'])
            dob=fake.date_between(start_date=date(1980, 1, 1), end_date=date(1995, 10, 12))
            join_date=fake.date_between(start_date=date(2015, 1, 1), end_date=date.today())

            education = Education.objects.create(
                school = generate_school_name(),
                bachelor_clg = generate_college_name(),
                masters_clg = generate_random_college_name(),
            )

            skills = Skills.objects.create(
                teacher_comm_skill = random.randint(80, 97),
                teacher_class_mgt_skill = random.randint(80, 97),
                teacher_creativity_skill = random.randint(80, 97),
                teacher_subj_skill = random.randint(80, 97),
            )


            # List of subjects for each level
            subjects_lkg_ukg = ['Pre-writing Skills', 'Drawing and Craft', 'Basic English', 'Basic Math', 'Environmental Studies']
            subjects_1_5 = ['English', 'Hindi', 'Mathematics', 'Science', 'Environmental Studies (EVS)', 'Social Studies (Introductory)', 'Computer Science (Basic)', 'Art and Craft', 'Physical Education (Sports)', 'Moral Science']
            subjects_6_8 = ['English', 'Hindi', 'Mathematics', 'Physics' , 'Chemistry', 'Biology', 'History', 'Geography', 'Civic','Computer Science', 'Physical Education', 'Moral Science', 'Art and Craft', 'Music']
            subjects_9_10 = ['English', 'Hindi', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Civics', 'Economics', 'Computer Science', 'Physical Education', 'Moral Science', 'Sanskrit', 'Art', 'Music',]

            # Example: Random subject selection for a student in LKG
            student_class = random.choice(['LKG', 'UKG', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

            if student_class in ['LKG', 'UKG']:
                subjects = random.sample(subjects_lkg_ukg, 1)  # Randomly pick 3 subjects
            elif student_class in ['1', '2', '3', '4', '5']:
                subjects = random.sample(subjects_1_5, 1)  # Randomly pick 3 subjects
            elif student_class in ['6', '7', '8']:
                subjects = random.sample(subjects_6_8, 1)  # Randomly pick 3 subjects
            else:
                subjects = random.sample(subjects_9_10, 1)  # Randomly pick 3 subjects

            # print(f"Class: {student_class}, Subjects: {subjects}")

            teacher_responsibility = Responsibility.objects.create(
                teacher_subj = ", ".join(subjects),
                teacher_class = student_class,
                teacher_section = random.choice(["A", "B", "C", "D"])
            )



            # teacher = Teacher.objects.create(
            #   teacher_name =fake.name_male(),
            #   father_occupation=fake.job(),
            #   father_mobile=fake.msisdn()[:10],
            #   father_email=fake.email(),
            #   mother_name=fake.name_female(),
            #   mother_occupation=fake.job(),
            #   mother_mobile=fake.msisdn()[:10],
            #   mother_email=fake.email(),
            #   present_address=fake.address(),
            #   permanent_address=fake.address(),
            # )

            qualifications = [
                "B.Ed. (Bachelor of Education)",
                "M.Ed. (Master of Education)",
                "Ph.D. in Education",
                "M.A. in Education",
                "B.A. in Education",
                "M.Sc. in Mathematics",
                "B.Sc. in Science",
                "M.A. in English",
                "M.A. in History",
                "M.A. in Geography",
                "M.A. in Political Science",
                "B.Tech in Computer Science",
                "M.Tech in Computer Science",
                "M.A. in Psychology",
                "B.A. in Physical Education",
                "Diploma in Special Education",
                "M.S.W. (Master of Social Work)",
                "B.A. in Fine Arts",
                "B.Ed. in Special Education"
            ]

            # Randomly select a qualification for a teacher
            

            Teacher.objects.create(
              teacher_id=f"TEACHER{1006 + i}",
              teacher_first_name=fake.first_name(),
              teacher_last_name=fake.last_name(),
              teacher_email=fake.email(),
              gender=gender,
              teacher_dob= str(dob),#fake.date_between(start_date='-16y', end_date='-6y'),
              teacher_mobile=fake.msisdn()[:10],
              teacher_join_date=str(join_date),#fake.date_between(start_date='2015-01-01', end_date='today'),
              teacher_qualification = random.choice(qualifications),
              teacher_experience=random.randint(3, 10),
              teacher_address = fake.address(),

              teacher_skills = skills,
              teacher_responsibility = teacher_responsibility,
              teacher_education = education,
              
            )

            

            # # student = Student.objects.create(
            #     first_name = fake.first_name(),
            #     last_name = fake.last_name(),
            #     email = fake.email(),
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
            #     parent.father_email = fake.email(),
            #     parent.mother_name = fake.name_female(),
            #     parent.mother_occupation = fake.job(),
            #     parent.mother_mobile = fake.msisdn()[0:10],
            #     parent.mother_email = fake.email(),
            #     parent.present_address = fake.address(),
            #     parent.permanent_address = fake.address()
            # )
        self.stdout.write(self.style.SUCCESS(f"Successfully added {total} teachers."))
