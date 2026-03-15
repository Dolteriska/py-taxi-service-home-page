from django.http import HttpResponse
from taxi.models import Driver, Manufacturer, Car
from django.shortcuts import render


def index(request) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()
    return render(request, "taxi/index.html", {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    })
