from django.contrib import admin

from .models import Person
from .models import Mark

admin.site.site_header = 'مدیریت وب سایت'

class PersonAdmin(admin.ModelAdmin):
    list_display =['melicode','fname']

class MarkAdmin(admin.ModelAdmin):
    list_display = ['person','grade']


admin.site.register(Person,PersonAdmin)
admin.site.register(Mark,MarkAdmin)
