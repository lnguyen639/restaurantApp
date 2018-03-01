from django.urls import path, reverse_lazy, re_path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('menu/add/', views.MenuItemCreateView.as_view(), name='menu_add'),
    path('menu/delete/<int:pk>', views.MenuItemDeleteView.as_view(), name='menu_delete'),
    path('orderwmenuitem/add/', views.OrderwMenuItemCreateView.as_view(), name='order_add'),
    path('order/add/', views.OrderCreateView.as_view(), name='order_add'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='menu_delete'),
    path('orderview/<int:pk>', views.orderview, name='order'),
    re_path(r'search/', views.MenuItemListView.as_view(), name='search'),
]