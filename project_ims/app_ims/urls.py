from django.urls import path
from . import views
urlpatterns = [
    path('items/', views.item_index, name="items.index"),
    path('items/create/', views.item_index, name="items.create"),
    path('items/edit/', views.item_index, name="items.edit"),
    path('items/show/', views.item_index, name="items.show"),

]
