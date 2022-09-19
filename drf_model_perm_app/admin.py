from django.contrib import admin
from drf_model_perm_app.models import Tool

# Register your models here.
class ToolAdmin(admin.ModelAdmin):
    """ Tool admin """
    list_display = ['id',
        'name',
    ]

admin.site.register(Tool, ToolAdmin)