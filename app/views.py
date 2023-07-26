from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import (
	authenticate, login as auth_login, logout
)
from django.views.decorators.http import require_POST

from .forms import (
    AppointmentForm, LoginForm, SearchAppointment
)
from .models import Patient, Appointment

import datetime as dt
import json


def logout_page(request):
	logout(request)
	return redirect('/marcar-consulta/')

def login_page(request):
	if request.user.is_authenticated:
		return redirect('/marcar-consulta/')

	error_message = ''
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			print(data)
			username = data.get('nome_do_usuario')
			password = data.get('palavra_passe')
			user = authenticate(
				request,
				username=username,
				password=password
			)
			if user is not None:
				auth_login(request, user)
				response = redirect('/marcar-consulta/')
				print(response['Location'])
				return response
			else:
				error_message = 'Nome de usuario or senha estao errados'
		else:
			print(form.errors)
	else:
		form = LoginForm()

	return render(request,
				  'app/login.html',
				  {'form': form, 'error_message': error_message})


@require_POST
def get_appointments_api(request):
	data = json.loads(request.body)
	# print(data)
	name = data.get('name')
	date = data.get('date')
	year, month, day = date.split('-')
	date = dt.date(int(year), int(month), int(day))

	appoints = []
	if name != 'Insira nome':
		patients = Patient.objects.filter(
			Q(first_name__contains=name) |
			Q(last_name__contains=name)
		)
		
		if patients.exists():
			for patient in patients:
				appoint = Appointment.objects.filter(
					patient=patient
				)
				for app in appoint:
					appoints.append(app.serialize())
	else:
		appoints_ = Appointment.objects.filter(
			date=date
		)
		if appoints_.exists():
			for app in appoints_:
				appoints.append(app.serialize())


	return JsonResponse({
		'data': appoints
	})


def appointmets(request):
	# appoints = []
	# if request.method == 'POST':
	# 	form = SearchAppointment(request.POST)
	# 	if form.is_valid():
	# 		data = form.cleaned_data
	# 		date = data.get('date')
	# 		appoints = Appointment.objects.filter(
	# 			date=date
    #         )
	# 		print(appoints)
	# 	else:
	# 		print(form.errors)
	# else:
		
	form = SearchAppointment()
		
	return render(request,
	              'app/appointmets.html',
                  {'form': form})


def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            phone_number = data.get('phone_number')
            disease = data.get('disease')
            date = data.get('date')
            priority = data.get('priority')
            patient = Patient.objects.filter(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number
            )
            if patient.exists():
                patient = patient.first()
                appoint = Appointment.objects.create(
                    patient=patient,
                    disease=disease,
                    date=date,
                    priority=priority
                )
                appoint.save()
                # print(json.dumps(appoint.serialize(), 
                #     indent=4, default=str))
            else:
                patient = Patient.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number
                )
                patient.save()
                appoint = Appointment.objects.create(
                    patient=patient,
                    disease=disease,
                    date=date,
                    priority=priority
                )
                appoint.save()
                # print(json.dumps(appoint.serialize(), 
                #     indent=4, default=str))
        else:
            print(form.errors)
    else:
        form = AppointmentForm()
    
    return render(request,
                  'app/make_appointment.html',
                  {'form': form})