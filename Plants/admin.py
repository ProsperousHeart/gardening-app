from django.contrib import admin
from .models import Plant, PlantLink

def duplicate_selected_plant(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Set primary key to None to create a new object
        obj.name_common = f"[COPY] {obj.name_common}"
        obj.save()

duplicate_selected_plant.short_description = "Duplicate selected items"

class PlantAdmin(admin.ModelAdmin):
    actions = [duplicate_selected_plant]

def duplicate_selected_link(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None  # Set primary key to None to create a new object
        obj.title = f"[COPY] {obj.title}"
        obj.save()

duplicate_selected_link.short_description = "Duplicate selected items"

class PlantLinkAdmin(admin.ModelAdmin):
    actions = [duplicate_selected_link]

# Register your models here.

admin.site.register(Plant, PlantAdmin)
admin.site.register(PlantLink, PlantLinkAdmin)