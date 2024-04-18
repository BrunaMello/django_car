from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import register_view, login_view, logout_view
from cars.views import CarListView, NewCarCreateView, CarDetailView, CarUpdateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('register/', register_view, name='register'),
                  path('login/', login_view, name='login'),
                  path('logout/', logout_view, name='logout'),
                  path('cars/', CarListView.as_view(), name='cars_list'),
                  path('new_car/', NewCarCreateView.as_view(), name='new_car'),
                  path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
                  path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
