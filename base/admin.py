from django.contrib import admin
from .models import Century, Alloma, Madrasa, AllomaMenu

@admin.register(Alloma)
class AllomaAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_year", "madrasa_alloma")
    list_filter = ("madrasa_alloma",)
    search_fields = ["name"]

@admin.register(AllomaMenu)
class AllomaMenuAdmin(admin.ModelAdmin):
    list_display = ("title", "logo")

@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    list_display = ("century", "sum_madrasa")

@admin.register(Madrasa)
class MadrasaAdmin(admin.ModelAdmin):
    list_display = ("name", "relevant_century")
    list_filter = ("relevant_century",)
    search_fields = ["name"]
