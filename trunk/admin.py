from django.contrib import admin
from .models import Subject, Subject_Info, Subject_Extra_Info

admin.site.site_header = "Islamic Civilisation Admin"
admin.site.site_title = "ICV Admin Portal"
admin.site.index_title = "ICV Boshqaruv Portaliga Xush kelibsiz!"

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "menu")
    list_filter = ("menu",)

@admin.register(Subject_Info)
class SubjectInfoAdmin(admin.ModelAdmin):
    list_display = ("text", "id", "subject")
    list_filter = ("subject",)

@admin.register(Subject_Extra_Info)
class SubjectExtraInfoAdmin(admin.ModelAdmin):
    list_display = ("text", "id", "subject")
    list_filter = ("subject",)