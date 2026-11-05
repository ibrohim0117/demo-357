from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from apps.views import home_view, book_list
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('books/', book_list, name='books')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
