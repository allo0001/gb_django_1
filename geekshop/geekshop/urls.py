from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp





urlpatterns = [
    path('', mainapp.index, name='index'),

    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('basket/', include('basketapp.urls', namespace='basketapp')),
    path('adminapp/', include('adminapp.urls', namespace='adminapp')),

    path('contact/', mainapp.contact, name='contact'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
