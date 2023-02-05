from django.contrib import admin

from .models import BotUser, BotAdmin, BotToken


class AdminBotUser(admin.ModelAdmin):
    list_display = ('tg_id', 'username', 'first_name')
    search_fields = ['tg_id', 'username', 'first_name']
    ordering = []


class AdminBotAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'name')
    search_fields = ['tg_id', 'name']
    ordering = []


class AdminBotToken(admin.ModelAdmin):
    list_display = ('token',)


admin.site.register(BotUser, AdminBotUser)
admin.site.register(BotAdmin, AdminBotAdmin)
admin.site.register(BotToken, AdminBotToken)
