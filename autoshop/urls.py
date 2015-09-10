# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0

from django.conf.urls import patterns, include, url
from django.contrib import admin
from autoshop import settings
from shop.views import index, mgmt_index, reg, lk, regsuccess, login_lk, login_page, restore_password, logout_lk, \
    PagesListView, PagesDetailView, PagesCreateView, PagesDeleteView, mgmt_index_pages, AboutCompanyEditView, \
    ForSuppliersEditView, DeliveryInfoEditView, ContactsEditView, FAQListView, FAQCreateView, FAQDeleteView, \
    FAQUpdateView, supp_index, SupplierListView, SupplierCreateView, SupplierDeleteView, SupplierUpdateView, \
    PriceListListView, pricelist_upload, pricelist_to_goods, PriceListDeleteView, MarkupListView, markup_create, \
    markup_edit, MarkupDeleteView, StockListView, create_stock, edit_stock, DeleteStockView, GoodsListView, \
    goods_mgmt_search, GoodsCreateView, GoodsUpdateView, GoodsDeleteView, dev_cat_list, DeveloperCreateView, \
    edit_developer, add_goods_to_developer, delete_dev_goods, DeveloperDeleteView, CategoryCreateView, edit_category, \
    add_goods_to_category, delete_cat_goods, CategoryDeleteView, ExportGoodsListView, create_new_export_goods, \
    Export1CDeleteView, order_index, ClientsListView, clients_search, EditClientView, change_client_password, \
    ClientDeleteView, OrdersListView, edit_order, add_goods_to_order, DeleteOrderView, BillsListView, change_bill, \
    show_bill, ExportOrderListView, create_new_export_orders, user_list, change_adm_user, change_admin_password, \
    DeleteUserView, admin_add, DeliveryListView, DeliveryMethodCreateView, DeliveryMethodsUpdateView, \
    DeliveryMethodDeleteView, search_goods, basket_actions, preview_order, choose_order_devmethod, choose_order_paymethod, \
    cash_order, edit_clients_lk, change_password_lk, lk_order, aboutcompany, forsuppliers, delivery_info, contacts, \
    faq_list, pages, FrontDeveloperListView, cat_list_with_dev, show_goods_cat_by_dev, org_registration_form, \
    CategoryPriceClientsListView, ClientsPriceCategoryUpdateView, PaymentMethodsListView, PaymentMethodCreateView, \
    PaymentsMethodsUpdateView, PaymentMethodDeleteView, load_photos, modal_good

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sinkai.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),
    url(r'^reg/$', reg, name='reg'),
    url(r'^org_reg/$', org_registration_form, name='org_reg'),
    url(r'^regsuccess/$', regsuccess, name='regsuccess'),
    url(r'^lk/$', lk, name='lk'),
    url(r'^login_lk/$', login_lk, name='login_lk'),
    url(r'^login/$', login_page, name='login_page'),
    url(r'^restore_password/$', restore_password, name='restore_password'),
    url(r'^logout/$', logout_lk, name='logout'),
    url(r'^search/$', search_goods, name='search'),
    url(r'^add_to_basket/$', basket_actions, name='basket'),
    url(r'^create_order/$', preview_order, name='preview-order'),
    url(r'^choose_methods/$', choose_order_devmethod, name='choose-methods'),
    url(r'^choose_pays/$', choose_order_paymethod, name='choose-pays'),
    url(r'^cash_order/$', cash_order, name='cash-order'),
    # url(r'^pay_robo/(?P<order_id>\d+)/$', pay_robokassa, name='pay-robo'),
    url(r'^edit-client/$', edit_clients_lk, name='lk-edit-client'),
    url(r'^change-pass-lk/$', change_password_lk, name='change-pass-lk'),
    url(r'^lk-order/(?P<pk>\d+)/$', lk_order, name='lk-order'),
    url(r'^about/$', aboutcompany, name='about'),
    url(r'^forsuppliers/$', forsuppliers, name='forsuppliers'),
    url(r'^delivery/$', delivery_info, name='delivery'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^faqs/$', faq_list, name='faqs'),
    url(r'^pages/(?P<slug>[^/]+)/$', pages, name='page'),
    url(r'^ourstore/$', FrontDeveloperListView.as_view(), name='our_store'),
    url(r'^ourstore/(?P<developer>\d+)/$', cat_list_with_dev, name='front_cat_list'),
    url(r'^ourstore/(?P<developer>\d+)/(?P<category>\d+)/$', show_goods_cat_by_dev, name='front_cat_dev_goods'),



    # Management url's
    url(r'^mgmt/$', mgmt_index, name='mgmt_index'),
    url(r'^mgmt/pages-index/$', mgmt_index_pages, name='pages-index'),
    url(r'^mgmt/aboutcompany-edit/(?P<pk>\d+)/$', AboutCompanyEditView.as_view(), name='aboutcompany-edit'),
    url(r'^mgmt/forsuppliers-edit/(?P<pk>\d+)/$', ForSuppliersEditView.as_view(), name='forsuppliers-edit'),
    url(r'^mgmt/deliveryinfo-edit/(?P<pk>\d+)/$', DeliveryInfoEditView.as_view(), name='deliveryinfo-edit'),
    url(r'^mgmt/contacts-edit/(?P<pk>\d+)/$', ContactsEditView.as_view(), name='contacts-edit'),
    url(r'^mgmt/faq-edit-list/$', FAQListView.as_view(), name='faq-edit-list'),
    url(r'^mgmt/faq-new/$', FAQCreateView.as_view(), name='faq-new'),
    url(r'^mgmt/faq-edit/(?P<pk>\d+)/$', FAQUpdateView.as_view(), name='faq-edit'),
    url(r'^mgmt/faq-delete/(?P<pk>\d+)/$', FAQDeleteView.as_view(), name='faq-delete'),
    url(r'^mgmt/pages_list/$', PagesListView.as_view(), name='pages-list'),
    url(r'^mgmt/pages_detail/(?P<pk>\d+)/$', PagesDetailView.as_view(), name='pages-detail'),
    url(r'^mgmt/pages_new/$', PagesCreateView.as_view(), name='pages-new'),
    url(r'^mgmt/pages-delete/(?P<pk>\d+)/$', PagesDeleteView.as_view(), name='pages-delete'),
    url(r'^mgmt/supp-index/$', supp_index, name='supp-index'),
    url(r'^mgmt/supp-list/$', SupplierListView.as_view(), name='supp-list'),
    url(r'^mgmt/supp-new/$', SupplierCreateView.as_view(), name='supp-new'),
    url(r'^mgmt/supp-delete/(?P<pk>\d+)/$', SupplierDeleteView.as_view(), name='supp-delete'),
    url(r'^mgmt/supp-edit/(?P<pk>\d+)/$', SupplierUpdateView.as_view(), name='supp-edit'),
    url(r'^mgmt/price-list/$', PriceListListView.as_view(), name='price-list'),
    url(r'^mgmt/price-list-delete/(?P<pk>\d+)/$', PriceListDeleteView.as_view(), name='price-list-delete'),
    url(r'^mgmt/price-list-new/$', pricelist_upload, name='price-list-new'),
    url(r'^mgmt/price-list-parse/$', pricelist_to_goods, name='price-list-parse'),
    url(r'^mgmt/markup-list/$', MarkupListView.as_view(), name='markup-list'),
    url(r'^mgmt/markup-new/$', markup_create, name='markup-new'),
    url(r'^mgmt/markup-edit/(?P<pk>\d+)/$', markup_edit, name='markup-edit'),
    url(r'^mgmt/markup-delete/(?P<pk>\d+)/$', MarkupDeleteView.as_view(), name='markup-delete'),
    url(r'^mgmt/stock-list/$', StockListView.as_view(), name='stock-list'),
    url(r'^mgmt/stock-new/$', create_stock, name='stock-new'),
    url(r'^mgmt/stock-edit/(?P<pk>\d+)/$', edit_stock, name='stock-edit'),
    url(r'^mgmt/stock-delete/(?P<pk>\d+)/$', DeleteStockView.as_view(), name='stock-delete'),
    url(r'^mgmt/goods-list/$', GoodsListView.as_view(), name='goods-list'),
    url(r'^mgmt/goods-search/$', goods_mgmt_search, name='goods-mgmt-search'),
    url(r'^mgmt/goods-new/$', GoodsCreateView.as_view(), name='goods-new'),
    url(r'^mgmt/goods-edit/(?P<pk>\d+)/$', GoodsUpdateView.as_view(), name='goods-edit'),
    url(r'^mgmt/goods-delete/(?P<pk>\d+)/$', GoodsDeleteView.as_view(), name='goods-delete'),
    url(r'^mgmt/goods-dev-cat-list/$', dev_cat_list, name='goods-dev-cat'),
    url(r'^mgmt/dev-new/$', DeveloperCreateView.as_view(), name='dev-new'),
    url(r'^mgmt/dev-edit/(?P<pk>\d+)/$', edit_developer, name='dev-edit'),
    url(r'^mgmt/dev-add-goods/$', add_goods_to_developer, name='dev-add-goods'),
    url(r'^mgmt/dev-del-goods/(?P<pk>\d+)/$', delete_dev_goods, name='del-dev-goods'),
    url(r'^mgmt/dev-delete/(?P<pk>\d+)/$', DeveloperDeleteView.as_view(), name='dev-delete'),
    url(r'^mgmt/cat-new/$', CategoryCreateView.as_view(), name='cat-new'),
    url(r'^mgmt/cat-edit/(?P<pk>\d+)/$', edit_category, name='cat-edit'),
    url(r'^mgmt/cat-add-goods/$', add_goods_to_category, name='cat-add-goods'),
    url(r'^mgmt/cat-del-goods/(?P<pk>\d+)/$', delete_cat_goods, name='cat-del-goods'),
    url(r'^mgmt/cat-delete/(?P<pk>\d+)/$', CategoryDeleteView.as_view(), name='cat-delete'),
    url(r'^mgmt/export-goods-list/$', ExportGoodsListView.as_view(), name='export-goods-list'),
    url(r'^mgmt/export-goods-new/$', create_new_export_goods, name='export-goods-new'),
    url(r'^mgmt/export-delete/(?P<pk>\d+)/$', Export1CDeleteView.as_view(), name='export-delete'),
    url(r'^mgmt/order-index/$', order_index, name='order-index'),
    url(r'^mgmt/clients-list/$', ClientsListView.as_view(), name='clients-list'),
    url(r'^mgmt/clients-search/$', clients_search, name='clients-search'),
    url(r'^mgmt/clients-edit/(?P<pk>\d+)/$', EditClientView.as_view(), name='clients-edit'),
    url(r'^mgmt/change-password/(?P<pk>\d+)/$', change_client_password, name='change-password'),
    url(r'^mgmt/clients-delete/(?P<pk>\d+)/$', ClientDeleteView.as_view(), name='clients-delete'),
    url(r'^mgmt/orders-list/$', OrdersListView.as_view(), name='orders-list'),
    url(r'^mgmt/orders-edit/(?P<pk>\d+)/$', edit_order, name='orders-edit'),
    url(r'^mgmt/add-goods-order/$', add_goods_to_order, name='add-goods-order'),
    url(r'^mgmt/orders-delete/(?P<pk>\d+)/$', DeleteOrderView.as_view(), name='orders-delete'),
    url(r'^mgmt/bills-list/$', BillsListView.as_view(), name='bills-list'),
    url(r'^mgmt/bill-edit/(?P<pk>\d+)/$', change_bill, name='bill-edit'),
    url(r'^mgmt/show-bill/(?P<pk>\d+)/$', show_bill, name='bill-show'),
    url(r'^mgmt/export-orders-list/$', ExportOrderListView.as_view(), name='export-orders-list'),
    url(r'^mgmt/export-orders-new/$', create_new_export_orders, name='export-orders-new'),
    url(r'^mgmt/user-list/$', user_list, name='user-list'),
    url(r'^mgmt/edit-user/(?P<pk>\d+)/$', change_adm_user, name='user-edit'),
    url(r'^mgmt/admin-pass/(?P<pk>\d+)/$', change_admin_password, name='admin-pass'),
    url(r'^mgmt/delete-user/(?P<pk>\d+)/$', DeleteUserView.as_view(), name='delete-user'),
    url(r'^mgmt/admin-add/$', admin_add, name='admin-add'),
    url(r'^mgmt/delivery-list/$', DeliveryListView.as_view(), name='delivery-list'),
    url(r'^mgmt/delivery-new/$', DeliveryMethodCreateView.as_view(), name='delivery-new'),
    url(r'^mgmt/delivery-edit/(?P<pk>\d+)/$', DeliveryMethodsUpdateView.as_view(), name='delivery-edit'),
    url(r'^mgmt/delivery-delete/(?P<pk>\d+)/$', DeliveryMethodDeleteView.as_view(), name='delivery-delete'),
    url(r'^mgmt/payments-list/$', PaymentMethodsListView.as_view(), name='payments-list'),
    url(r'^mgmt/payments-new/$', PaymentMethodCreateView.as_view(), name='payments-new'),
    url(r'^mgmt/payments-edit/(?P<pk>\d+)/$', PaymentsMethodsUpdateView.as_view(), name='payments-edit'),
    url(r'^mgmt/payments-delete/(?P<pk>\d+)/$', PaymentMethodDeleteView.as_view(), name='payments-delete'),
    url(r'^mgmt/client-price-cat/$', CategoryPriceClientsListView.as_view(), name='client-price-cat'),
    url(r'^mgmt/client-price-cat-edit/(?P<pk>\d+)/$', ClientsPriceCategoryUpdateView.as_view(), name='client-price-cat-edit'),
    url(r'^mgmt/load-photos/$', load_photos, name='load_photos'),
    url(r'^modal_good/(?P<pk>\d+)/$', modal_good, name='modal_good'),

    # Service urls
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robokassa/', include('robokassa.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
)
