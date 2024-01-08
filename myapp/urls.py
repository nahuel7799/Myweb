from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    # Configurar las URLs para la clase Page
    # ...
]

# En templates/crear un template para cada vista

from django.urls import path
from . import views

urlpatterns = [
    path('pages/', views.page_list, name='page_list'),
    path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
    # Agregar URLs para las vistas de autenticación y administración
    # ...
]

# Crear templates para cada vista (page_list.html, page_detail.html, create_blog.html, edit_blog.html, delete_blog.html, admin_dashboard.html)

from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('blogs/<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),
    path('blogs/<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # Agregar las URLs para la clase Page si es necesario
    # path('pages/', views.page_list, name='page_list'),
    # path('pages/<int:page_id>/', views.page_detail, name='page_detail'),
    # ...
]
