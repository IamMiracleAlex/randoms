from django.contrib import admin

from randoms.models import Random


@admin.register(Random)
class RandomAdmin(admin.ModelAdmin):
    search_fields = ['uuid']
    list_display = ['uuid', 'date']