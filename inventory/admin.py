import csv
from django.contrib import admin
from django.http import HttpResponse

from inventory.models import Category, Product, StockMovement


class StockMovementInline(admin.TabularInline):
    model = StockMovement
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'stock', 'price')
    search_fields = ('name', 'sku')
    list_filter = ('category',)
    inlines = [StockMovementInline]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')  # Fix N+1

    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=products.csv'
        writer = csv.writer(response)
        writer.writerow(['Name', 'SKU', 'Category', 'Stock', 'Price'])
        for obj in queryset:
            writer.writerow([obj.name, obj.sku, obj.category.name, obj.stock, obj.price])
        return response

    export_to_csv.short_description = "Export selected products to CSV"


admin.site.register(Category)
