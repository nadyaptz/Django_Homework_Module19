from django.contrib import admin
from .models import Buyer, Game, News

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('username', 'balance', 'age',)
    search_fields = ('username', )
    list_filter = ('balance', 'age',)
    list_per_page = 30
    readonly_fields = ('balance',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    search_fields = ('title', )
    list_filter = ('size', 'cost',)
    list_per_page = 20


admin.site.register(News)
