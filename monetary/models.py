from django.db import models

# Create your models here.
class Fees(models.Model):
  student_id = models.CharField(max_length=50)
  student_name = models.CharField(max_length=100)
  gender = models.CharField(max_length=50, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])

  fees_choices = [("Select Type", "Select Type"),("Academic Fees", "Academic Fees"), ("Class Test Fee", "Class Test Fees"), ("Exam Fees", "Exam Fees"), ("Hostel Fees", "Hostel Fees"), ("Transport Fees", "Transport Fees"), ("Mess Fees", "Mess Fees"), ("Miscellaneous Fees", "Miscellaneous Fees")]
  fees_type = models.CharField(max_length=50, choices=fees_choices)

  fees_amount = models.CharField(max_length=100)
  paid_date = models.DateField(auto_now_add=True)
  paid_status = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.student_id}-{self.fees_type}-{self.fees_amount}"
  
class Salary(models.Model):
  staff_id = models.CharField(max_length=50)
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=20, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
  join_date = models.DateField()
  salary_amount = models.CharField(max_length=50)
  # salary_paid_date = models.DateField(auto_now_add=True)
  status = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.staff_id}-{self.salary_amount}"
  