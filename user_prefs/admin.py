from django.contrib import admin

from user_prefs.models import Prefs


# Register your models here.
@admin.register(Prefs)
class PrefsAdmin(admin.ModelAdmin):
    pass