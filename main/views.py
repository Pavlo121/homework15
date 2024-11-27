from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, 'main/home.html', {'title': 'Головна сторінка'})

def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})

class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html', {'title': 'Контакти'})

class ServiceView(View):
    def get(self, request):
        services = ['Веб-розробка', 'SEO', 'Дизайн', 'Консалтинг']
        return render(request, 'main/services.html', {'title': 'Послуги', 'services': services})
