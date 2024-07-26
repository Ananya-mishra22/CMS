from django.contrib import admin
from Home.models import classroom_booked,feedback,dt,is_student,complaint

# Register your models here.
admin.site.register(classroom_booked)
admin.site.register(feedback)
admin.site.register(dt)
admin.site.register(is_student)
admin.site.register(complaint)