from django.urls import path
from homepage import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),

    # Login & Signup page
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),

    # Products page
    path('products', views.products, name='products'),
    path('add_products', views.add_products, name='add_products'),
    path('update_products/<str:pk>/', views.update_products,name='update_products'),
    path('delete_products/<str:pk>/', views.delete_products,name='delete_products'),

    # Items page
    path('items', views.items, name='items'),
    path('add_items', views.add_items, name='add_items'),
    path('update_item/<str:pk>/', views.update_item,name='update_item'),
    path('delete_item/<str:pk>/', views.delete_item,name='delete_item'),

    # Checkout page
    path('productCheckout', views.productCheckout, name='productCheckout' ),
    path('add_productCheckout', views.add_productCheckout, name='add_productCheckout'),
    path('update_productInvoice/<str:pk>/', views.update_productInvoice,name='update_productInvoice'),
    path('delete_productInvoice/<str:pk>/', views.delete_productInvoice,name='delete_productInvoice'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)