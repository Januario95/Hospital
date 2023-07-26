from django.urls import path

from .views import (
    make_appointment, logout_page, login_page,
    appointmets, get_appointments_api,
)

app_name = 'app'


urlpatterns = [
    path('marcacoes/', appointmets, name='marcacoes'),
    path('marcar-consulta/', make_appointment,
         name='make_appointment'),

    # APIs
    path('get_appointments_api/', get_appointments_api),

    path('logout/', logout_page, name='logout'),
    path('login/', login_page,
		 name="login"),
]