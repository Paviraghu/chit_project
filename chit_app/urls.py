from django.urls import path
from .views import register_chit, success, view_chits,edit_chit,handle_week,handle_payment

urlpatterns = [
    path('', register_chit, name='register_chit'),
    path('success/', success, name='success'),
    path('view_chits/', view_chits, name='view_chits'),
    path('edit_chit/<int:chit_id>/', edit_chit, name='edit_chit'),
    path('handle_week/<int:chit_id>/<int:week>/', handle_week, name='handle_week'),
    path('handle_payment/<int:chit_id>/', handle_payment, name='handle_payment'),
]