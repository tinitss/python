from django.urls import path
from MiApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('servicios/', views.servicios, name='Servicios'),
    path('tienda/', views.tienda, name='Tienda'),
    path('blog/', views.blog, name='Blog'),
    path('contacto/', views.contacto, name='Contacto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)