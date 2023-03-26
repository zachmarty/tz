from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('<path:p>', views.menu, name = 'menu')
]

