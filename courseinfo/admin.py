from django.contrib import admin
from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class InstructorInline(admin.StackedInline):
    model = Instructor
    can_delete = False
    verbose_name_plural = 'instructor'


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


class UserAdmin(BaseUserAdmin):
    inlines = (InstructorInline, StudentInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Period)
admin.site.register(Year)
