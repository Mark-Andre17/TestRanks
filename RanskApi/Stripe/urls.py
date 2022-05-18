from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('buy/<int:item_pk>', buy_items),
    path('item/<int:item_pk>', get_item),
]
