from django.contrib import admin
from employee import models


class UnderagesFiles(admin.TabularInline):
    fk_name = "underages"
    model = models.UnderageFile
    extra = 1


@admin.register(models.Underages)
class UnderagesAdmin(admin.ModelAdmin):
    list_display = ("pk", "full_name")

    inlines = [UnderagesFiles]


admin.site.register(models.Role)
admin.site.register(models.FamilyStatus)
admin.site.register(models.Handicapped)
admin.site.register(models.Illness)
admin.site.register(models.Employee)
