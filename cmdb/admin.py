from django.contrib import admin
from cmdb.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_time', 'categories', 'title', 'last_edit_time')
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
