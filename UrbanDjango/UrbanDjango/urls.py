from django.contrib import admin
from django.urls import path
from task2.views import func_view, ClassView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', ClassView.as_view()),
    path('', func_view),  # Корневой маршрут
    path('functional/', func_view),  # Новый маршрут для /functional/
]
