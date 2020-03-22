from django.contrib import admin

from .models import pastor

class pastorsAdmin(admin.ModelAdmin):
    list_display=('id','name','email','church')
    list_display_links=('id','name')
    search_fields=('name',)
    list_per_page=25

admin.site.register(pastor,pastorsAdmin)

