from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'user', 'status', 'created_at')
    list_filter = ('status', 'project', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at',)