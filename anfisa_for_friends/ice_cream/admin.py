from django.contrib import admin

# Register your models here.

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

# ...и регистрируем её в админке:
admin.site.register(Topping)
admin.site.register(Wrapper)

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


admin.site.register(Category, CategoryAdmin) 


admin.site.register(IceCream, IceCreamAdmin)
admin.site.empty_value_display = 'Не задано'
