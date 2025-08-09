# teachera/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


# We’ll import each app’s ViewSets once we define them
# from accounts.views import ...
# from opportunities.views import ...
# from resources.views import ...
# from nominations_awards.views import ...
# from feedback_discussion.views import ...

router = routers.DefaultRouter()
# Example (we’ll uncomment these once the viewsets exist):
# router.register(r'users', UserViewSet)
# router.register(r'opportunities', OpportunityViewSet, basename='opportunity')
# router.register(r'resources', ResourceViewSet, basename='resource')
# router.register(r'nominations', NominationViewSet, basename='nomination')
# router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path("api/opportunities/", include("opportunities.urls")),
    path("api/resources/", include("resources.urls")),
    path("api/feedback/", include("feedback_discussion.urls")),
    path("api/nominations/", include("nominations_awards.urls")),
    path("api/signup/", include("signup.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
