from django.contrib import admin



from .models import News


class newsAdmin(admin.ModelAdmin):
    # ...
    list_display = ('title', 'category', 'pub_date')

admin.site.register(News,newsAdmin)