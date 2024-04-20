from django.contrib import admin
from schedule.models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
