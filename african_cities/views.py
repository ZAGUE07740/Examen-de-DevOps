from django.shortcuts import render
from african_cities.models import City

def city_list(request):
    cities = City.objects.all()
    return render(request, 'african_cities/city_list.html', {'cities': cities})
