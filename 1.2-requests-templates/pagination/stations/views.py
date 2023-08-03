
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(data, 20)
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)