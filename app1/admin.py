from django.contrib import admin

from app1.models import App1


@admin.register(App1)
class App1Admin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )
