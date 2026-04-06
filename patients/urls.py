from django.urls import path
from .views import patient_delete, patient_list, patient_edit, patient_create

urlpatterns = [
    path('', patient_list),
    path('<int:pk>/edit', patient_edit),
    path('<int:pk>/delete', patient_delete),
    path('create/', patient_create)
]