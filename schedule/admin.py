from django.contrib import admin
from schedule.models import Schedule, Group, Subject, ScheduleType


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ScheduleType)
class ScheduleTypeAdmin(admin.ModelAdmin):
    pass