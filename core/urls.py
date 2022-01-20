from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from .views import HomeView, UserProductListView, ProductUpdateView, ProductDetailView

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('users/', include('accounts.urls', namespace='users')),

    path('', HomeView.as_view(), name='home'),
    path('products/', UserProductListView.as_view(), name='product-list'),
    path('products/<slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<slug>/update/', ProductUpdateView.as_view(), name='product-update'),
    path("__reload__/", include("django_browser_reload.urls")),

    path('smarket/', include('smarket.urls', namespace='smarket'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL)
