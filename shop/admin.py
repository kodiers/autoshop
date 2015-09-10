# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0

from django.contrib import admin
from shop.models import Developer, Supplier, PriceList, GoodsCategory, Goods, Markup, Stock, Export1C, Clients, Orders, \
    OrderDetails, Bills, Pages, Contacts, AboutCompany, ForSuppliers, DeliveryInfo, Basket, DeliveryMethods, \
    PaymentsMethods, ClientsPriceCategory

# Register your models here.

# --------- Fixes bug 17.04.2015 --------
class ClientsPriceCategoryAdmin(admin.ModelAdmin):
    """
    Admin class for clients category model
    """
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(ClientsPriceCategoryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

# --------- end ---------------------------


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for Contacts model
    """
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(ContactAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class AboutCompanyAdmin(admin.ModelAdmin):
    """
    Admin class for AboutCompany model
    """
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(AboutCompanyAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ForSuppliersAdmin(admin.ModelAdmin):
    """
    Admin class for ForSuppliers model
    """
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(ForSuppliersAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class DeliveryInfoAdmin(admin.ModelAdmin):
    """
    Admin class for DeliveryInfo
    """
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(DeliveryInfoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Developer)
admin.site.register(Supplier)
admin.site.register(PriceList)
admin.site.register(GoodsCategory)
admin.site.register(Goods)
admin.site.register(Markup)
admin.site.register(Stock)
admin.site.register(Export1C)
admin.site.register(ClientsPriceCategory, ClientsPriceCategoryAdmin)
admin.site.register(Clients)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Bills)
admin.site.register(Pages)
admin.site.register(Contacts, ContactAdmin)
admin.site.register(AboutCompany, AboutCompanyAdmin)
admin.site.register(ForSuppliers, ForSuppliersAdmin)
admin.site.register(DeliveryInfo, DeliveryInfoAdmin)
admin.site.register(Basket)
admin.site.register(DeliveryMethods)
admin.site.register(PaymentsMethods)