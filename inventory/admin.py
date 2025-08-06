import csv
from django.contrib import admin
from django.http import HttpResponse
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import (
    AutocompleteSelectFilter
)

from inventory.models import Category, Product, StockMovement


@admin.register(StockMovement)
class StockMovementAdmin(ModelAdmin):
    list_display = ('id', 'type', 'timestamp', 'quantity', 'product')
    list_filter = ('type', 'timestamp')
    search_fields = ('id',)
    autocomplete_fields = [
        'product'
    ]


class StockMovementInline(TabularInline):
    model = StockMovement
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id', 'name', 'category', 'stock', 'price')
    search_fields = ('id', 'name', 'sku')
    list_filter = (
        ["category", AutocompleteSelectFilter],
    )
    inlines = [StockMovementInline]
    autocomplete_fields = [
        'category',
    ]

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


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

    search_fields = [
        'id',
        'name',
    ]
