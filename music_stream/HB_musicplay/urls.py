from . import views
from django.urls import path
from django.urls import path

from . import views
from django.urls import path
from HB_musicplay import views
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
app_name = 'HB_musicplay'
schema_view = get_schema_view(
    openapi.Info(
        title="Hb_musicplay API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('songs/', views.SongList.as_view(), name='songs'),
    path('Song/', views.SongList.as_view(), name='Song'),
    path('users/', views.UserList.as_view(), name='users'),
    path('playlist/', views.ApiPlaylist.as_view(), name='playlist'),
    path('Artist/', views.ArtistList.as_view(), name='Artist'),


    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('base', views.base_view, name='base'),


    path('create_playlist/', views.create_playlist_view, name='create_playlist'),
    path('playlists/', views.playlists_view, name='playlists'),
    # path('playlist/<int:playlist_id>/', views.playlist_detail_view, name='playlist_detail'),


]

