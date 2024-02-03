from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from .views import FileUploadView, FileViewSet

app_name = 'api'

# pip install django-rest-swagger
# pip install drf-yasg
# add to settings INSTALLED_APPS = []
# 'rest_framework_swagger',
# 'drf_yasg'
# register urls
schema_view = get_schema_view(
    openapi.Info(
        title="DRF Upload Files",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register('files', FileViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view()),
    path('docs/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui')
]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
