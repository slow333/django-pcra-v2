<<<<<<< HEAD
from django.urls import path
from . import views

# apps/idol/
urlpatterns = [
    path('', views.idol_home, name='idol-home'),
    path('upload/', views.upload, name='idol-upload'),
    path('<int:pk>/detail', views.detail, name='idol-detail'),
    path('<int:pk>/delete', views.delete, name='idol-delete'),
    path('<int:pk>/update', views.update, name='idol-update'),
]
=======
from django.urls import path
from . import views
from .views import IdolListView, IdolDetailView, IdolUpdateView, IdolCreateView, IdolDeleteView

# idol/
urlpatterns = [
    path('', IdolListView.as_view(), name='idol-home'),
    # path('', views.idol_home, name='idol-home'),
    # path('<int:pk>/detail/', IdolDetailView.as_view(), name='idol-detail'),
    path('<int:pk>/update/', IdolUpdateView.as_view(), name='idol-update'),
    path('create/', IdolCreateView.as_view(), name='idol-upload'),
    path('<int:pk>/delete/', IdolDeleteView.as_view(), name='idol-delete'),
    # path('upload/', views.upload, name='idol-upload'),
    path('<int:pk>/detail', views.detail, name='idol-detail'),
    # path('<int:pk>/delete', views.delete, name='idol-delete'),
    # path('<int:pk>/title-update', views.delete, name='idol-title-update'),
]
>>>>>>> 5cfd106dbc2f54bb5d33a8ff7acb54b2c0160108
