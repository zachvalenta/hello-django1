from django.contrib import admin

from zjvapp.models import Thing


class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description', 'slug')  # fields for display in admin
    prepopulated_fields = {'slug': ('name', )}  # fields to use for slug

admin.site.register(Thing, ThingAdmin)
