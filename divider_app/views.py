from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def divide(request):
    try:
        x = float(request.GET.get('x'))
        y = float(request.GET.get('y'))

        if y == 0:
            return JsonResponse({'error': "You can't divide by 0!"}, status=400)

        result = x / y
        return JsonResponse({'result': result}, status=200)

    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid input. Please provide valid numbers for x and y.'}, status=400)

