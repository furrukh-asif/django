from django.shortcuts import render
from django.http import HttpResponse

def get_transaction(request, id=None):
    message = f'You submitted {id}'
    return HttpResponse(message)

