from urllib.parse import urlparse
from django.urls import path
from . import views
from django.conf import settings # Importing settings to see images in html
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.start, name="start" ),
    path('about', views.about, name="about" ),
    path('menu', views.menu, name="menu" ),
    path('menu/create', views.create, name="create" ),
    path('menu/edit', views.edit_dish, name="edit" ),
    path('delete/<int:id>', views.delete_dish, name="delete" ),
    path('menu/edit/<int:id>', views.edit_dish, name="edit" ),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)