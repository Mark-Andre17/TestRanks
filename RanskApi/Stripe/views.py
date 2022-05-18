import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import stripe
from .models import *
from django.shortcuts import render

key = os.environ['key']
stripe.api_key = key


def buy_items(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/admin',
            cancel_url='http://127.0.0.1:8000/admin',
        )
    return JsonResponse({'session_id': session.id})


def get_item(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    return render(request, 'Stripe/get_item.html', {'item': item})


