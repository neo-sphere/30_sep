from django.contrib import admin

from .models import Category

# admin.site.register(Category) # old fasion 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created', 'updated', 'is_active')
    date_hierarchy = 'updated'
    list_editable = ('is_active',)
    list_filter = ('created', 'updated', 'is_active')
    search_fields = ('name','slug')
    ordering = ('-updated',  )
    list_per_page = 2
    prepopulated_fields = {"slug": ("name",'is_active')}

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('name', 'slug', 'created', 'updated', 'is_active')
        else:
            return ('name', 'slug','updated')