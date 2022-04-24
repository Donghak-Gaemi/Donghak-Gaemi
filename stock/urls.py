from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'stock'

urlpatterns = [
    path('', views.home, name = 'list'),
    path('detail/<int:id>', views.detail_stock_news, name = "detail"),
    path('detail/ai/<int:id>', views.detail_ai, name = 'detail_ai'),
    path('detail/<int:id>/ai/$', views.detail_ai, name = "ai"),
]