from django.shortcuts import render
from django.http import HttpResponse
from .models import User, DeviceState
from .constants import BATTERY_MODES


def index(request):
    return render(request, 'main/Main.html')


def parse_request(request):

    response = {}
    if request.method == 'POST':

        action = request.POST.get('action')
        parameters = request.POST.get('parameters')

        if action == 'getTemperature':
            response = get_temperature(parameters)
        elif action == 'changeBatteryMode':
            response = change_battery_mode(parameters)
        elif action == 'changeTemperatureLimit':
            response = change_temperature_limit(parameters)

    if response == {}:        
        response['succes'] = 'false'
        response['result'] = ''

    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


def get_temperature(parameters):
    response_data = {}
    try:
        user = User.objects.filter(login='test')
        ds = DeviceState.objects.filter(user=user)
        temp = ds.temperature

        response_data['succes'] = 'true'
        response_data['result'] = str(temp)

    except (KeyError, Choice.DoesNotExist):
        response_data['succes'] = 'false'
        response_data['result'] = ''

    return response_data


def change_battery_mode(parameters):
    response_data = {}
    try:
        battery_mode = parameters['mode']
        if mode in BATTERY_MODES:
            user = User.objects.filter(login='test')
            ds = DeviceState.objects.filter(user=user)
            ds.mode = battery_mode
            ds.save()

            response_data['succes'] = 'true'
            response_data['result'] = ''

    except (KeyError, Choice.DoesNotExist):
        response_data = {}

    return response_data


def change_temperature_limit(parameters):
    response_data = {}
    try:
        temp_limit = parameters['limit']

        user = User.objects.filter(login='test')
        ds = DeviceState.objects.filter(user=user)
        ds.temperature_limit = temp_limit
        ds.save()

        response_data['succes'] = 'true'
        response_data['result'] = ''

    except (KeyError, Choice.DoesNotExist):
        response_data['succes'] = 'false'
        response_data['result'] = ''

    return response_data
