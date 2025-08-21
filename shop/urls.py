from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:cat>', views.category, name='category'),
    path('category/', views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
    path('orders/', views.user_orders, name='orders'),
    path('orders_details/<int:pk>', views.orders_details, name='orders_details')
]
