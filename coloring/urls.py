from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('home_page', views.home_page, name='home_page'),
    path('choose_a_theme', views.choose_a_theme, name='choose_a_theme'),
    path('free_drawing', views.free_drawing, name='free_drawing'),
    path('my_gallary', views.my_gallary, name='my_gallary'),
    path('drawing', views.drawing, name='drawing'),
    path('original_drawing', views.original_drawing, name='original_drawing')
]
