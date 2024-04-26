from django.urls import path
from .views.auth_views import LogoutView,LoginView,logout_then_login
from .views import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('login-user/', LoginView.as_view(), name='login_user'),
    path('logout-user/', logout_then_login, name='logout_user'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('book-list/', views.BookListView.as_view(), name='book_list'),
    path('orders-recieved/', views.OrderListView.as_view(), name='order_list'),
    path('orders-details/<int:pk>/', views.OrderDetailsView.as_view(), name='order_details'),
    path('myorders/', views.MyOrderListView.as_view(), name='my_order_list'),
    path('product-list/', views.ProductListView.as_view(), name='product_list'),
    path('book-detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('add-book/', views.BookCreateView.as_view(), name='add_book'),
    path('add-to-cart/', views.add_to_cart_view, name='add_to_cart'),
    path('user-cart/', views.UserCartView.as_view(), name='user_cart'),
    path('user-checkout/', views.UserCheckoutView.as_view(), name='user_checkout'),
    path('remove-from-cart/', views.remove_from_cart_view, name='remove_from_cart'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('address-list/', views.AddressListView.as_view(), name='address_list'),
    path('address/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),
    path('address/add/', views.AddressCreateView.as_view(), name='address_add'),
    path('address/<int:pk>/update/', views.AddressUpdateView.as_view(), name='address_update'),
    path('address/<int:pk>/delete/', views.AddressDeleteView.as_view(), name='address_delete'),
    path('place-order', views.place_order, name="place_order"),
    path('order-success', views.OrderSuccessView.as_view(), name="order_success"),
    path('gallery', views.media_gallery, name="gallery"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
