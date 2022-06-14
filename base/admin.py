from django.contrib import admin
from .models import Century, Alloma, Madrasa, AllomaMenu, Regions, SumMadrasa, MadrasaName

@admin.register(Alloma)
class AllomaAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_year", "madrasa_alloma")
    list_filter = ("madrasa_alloma",)
    search_fields = ["name"]
    ordering = ['id']


@admin.register(AllomaMenu)
class AllomaMenuAdmin(admin.ModelAdmin):
    list_display = ("title", "logo")
    ordering = ['id']


@admin.register(Century)
class CenturyAdmin(admin.ModelAdmin):
    list_display = ("century",)
    ordering = ['id']


@admin.register(MadrasaName)
class MadrasaNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    ordering = ['id']

    
@admin.register(Madrasa)
class MadrasaAdmin(admin.ModelAdmin):
    list_display = ("madrasa_id", "century_id")
    list_filter = ("century_id",)
    search_fields = ["madrasa_id"]
    ordering = ['id']


@admin.register(Regions)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ["name"]
    ordering = ['id']


@admin.register(SumMadrasa)
class SumMadrasaAdmin(admin.ModelAdmin):
    list_display = ("id", "region_id", "century_id", "sum_madrasa")
    list_filter = ("region_id", "century_id")
    search_fields = ["region_id", "century_id", "sum_madrasa"]
    ordering = ['id']

