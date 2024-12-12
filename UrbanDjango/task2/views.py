from django.shortcuts import render
from django.views.generic.base import TemplateView


# Функциональное представление
def func_view(request):
    return render(request, 'second_task/func_template.html')


# Классовое представление
class ClassView(TemplateView):
    template_name = 'second_task/class_template.html'
