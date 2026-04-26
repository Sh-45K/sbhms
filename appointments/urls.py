# from django.urls import path
# #from .views import appointment_list
# from .views import AppointmentListView, edit_appointment

# urlpatterns = [
#     path('', AppointmentListView.as_view()),
#     path('<int:id>/edit/', edit_appointment),
# ]



from django.urls import path
from .views import (
    AppointmentListView,
    create_appointment,
    edit_appointment,
    delete_appointment
)

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointments'),
    path('create/', create_appointment, name='create_appointment'),
    path('<int:id>/edit/', edit_appointment, name='edit_appointment'),
    path('<int:id>/delete/', delete_appointment, name='delete_appointment'),
]