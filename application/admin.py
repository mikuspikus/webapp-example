from django.contrib import admin

from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    fields = 'name', 'surname', 'phone', 'applied_at'
    readonly_fields = ('applied_at',)

admin.site.register(Application, ApplicationAdmin)