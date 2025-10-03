# # teachera/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve
# from django.urls import re_path

# router = routers.DefaultRouter()


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),
#     path("api/opportunities/", include("opportunities.urls")),
#     path("api/resources/", include("resources.urls")),
#     path("api/feedback/", include("feedback_discussion.urls")),
#     path("api/nominations/", include("nominations_awards.urls")),
#     path("api/signup/", include("signup.urls")),
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#     ]


from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path("api/opportunities/", include("opportunities.urls")),
    path("api/resources/", include("resources.urls")),
    path("api/feedback/", include("feedback_discussion.urls")),
    path("api/nominations/", include("nominations_awards.urls")),
    path("api/signup/", include("signup.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),]

# Media files (uploads)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Static files (CKEditor, admin CSS, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
CKEDITOR_5_CUSTOM_PATH = "django_ckeditor_5/dist/bundle.js"
CKEDITOR_5_CUSTOM_CSS = "django_ckeditor_5/dist/styles.css"