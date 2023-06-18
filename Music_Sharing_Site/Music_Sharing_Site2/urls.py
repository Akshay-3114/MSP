from django.urls import re_path
from django.views.defaults import page_not_found
from django.contrib import admin
from django.urls import path,include
import music.urls,users.urls
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('users/',include(users.urls)),
    path('music/',include(music.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
