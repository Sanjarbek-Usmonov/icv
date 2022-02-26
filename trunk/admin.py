from django.contrib import admin
from .models import Subject, Subject_Info, Subject_Extra_Info, Books, WoScience

admin.site.site_header = "Islamic Civilisation Admin"
admin.site.site_title = "ICV Admin Portal"
admin.site.index_title = "ICV Boshqaruv Portaliga Xush kelibsiz!"

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "menu")
    list_filter = ("menu__name",)

@admin.register(Subject_Info)
class SubjectInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "subject")
    list_filter = ("subject__name",)

@admin.register(Subject_Extra_Info)
class SubjectExtraInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "subject")
    list_filter = ("subject__text",)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author_id")
    list_filter = ("author_id__name",)
    search_fields = ["name", "author_id__name"]

@admin.register(WoScience)
class WoScienceAdmin(admin.ModelAdmin):
    list_display = ("info", "author_id")
    list_filter = ("author_id__name",)
    search_fields = ["info", "author_id__name"]
