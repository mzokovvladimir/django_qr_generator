from django.shortcuts import render
from websites.models import Websites


def home_view(request):
    name = "Welcome to"
    obj = Websites.objects.get(id=3)

    context = {
        'name': name,
        'obj': obj,
    }
    print(context)
    return render(request, 'websites/home.html', context)