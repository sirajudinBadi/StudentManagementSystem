from django.contrib import admin
from .models import Events, Happenings, TeacherLesson


# Register your models here.
admin.site.register(Events)
admin.site.register(Happenings)
admin.site.register(TeacherLesson)