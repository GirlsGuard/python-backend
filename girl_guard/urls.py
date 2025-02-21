from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from girl_guard import settings


schema_view = get_schema_view(
    openapi.Info(
        title='shop api',
        description='makers',
        default_version='v1'
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('account.urls')),
    path("api/side/", include("side.urls"))
]