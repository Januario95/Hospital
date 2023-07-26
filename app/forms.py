from django import forms
from django.utils import timezone

from ._helpers import PRIORITY


class MonthInput(forms.DateInput):
    input_type = 'month'
    format = '%d-%m-%Y'

class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%d-%m-%Y'


class SearchAppointment(forms.Form):
    SEARCH_TYPE = (
        ('...', '...'),
        ('Name', 'Name'),
        ('Date', 'Date')
	)
    search_by = forms.ChoiceField(
         choices=SEARCH_TYPE
	)
    patient_name = forms.CharField(
         required=False,
		max_length=50,
		widget=forms.TextInput(attrs={
			'value': 'Insira nome',
			'placeholder': 'Nome de paciente',
			'oninvalid': "this.setCustomValidity('Por favor insira o seu nome de paciente')"
		}
	))
    date = forms.CharField(
		max_length=255,
        required=False,
		widget=DateInput
    )

class LoginForm(forms.Form):
	nome_do_usuario = forms.CharField(
		max_length=50,
		widget=forms.TextInput(attrs={
			'value': 'januario95',
			'placeholder': 'Nome de usuario',
			'oninvalid': "this.setCustomValidity('Por favor insira o seu nome de usuario')"
		}
	))
	palavra_passe = forms.CharField(
		max_length=50,
		widget=forms.PasswordInput(attrs={
			'value': 'Jaci1995',
			'placeholder': 'Palavra passe',
			'oninvalid': "this.setCustomValidity('Por favor insira a sua senha aqui')"
		}
	))


class AppointmentForm(forms.Form):
    first_name = forms.CharField(
		max_length=150,
        required=True,
		widget=forms.TextInput(attrs={
            'value': 'Reinata',
			'placeholder': 'Insira o seu primeiro nome',
			'oninvalid': "this.setCustomValidity('Por favor insira seu primeiro nome aqui')"
		}))
    last_name = forms.CharField(
		max_length=150,
        required=True,
		widget=forms.TextInput(attrs={
            'value': 'Cipriano',
			'placeholder': 'Insira o seu ultimo nome',
			'oninvalid': "this.setCustomValidity('Por favor insira seu ultimo nome aqui')"
		}))
    email = forms.CharField(
		max_length=150,
        required=False,
		widget=forms.EmailInput(attrs={
            'value': 'januario.cipriano@ayamed.co.mz',
			'placeholder': 'Insira o seu email',
			'oninvalid': "this.setCustomValidity('Por favor insira seu email aqui')"
		}))
    phone_number = forms.CharField(
		max_length=255,
        required=True,
		widget=forms.TextInput(attrs={
            'value': '865482431',
			'placeholder': 'Insira o seu numero de telefone',
			'oninvalid': "this.setCustomValidity('Por favor insira seu numero de telefone aqui')"
		}))
    disease = forms.CharField(
		max_length=255,
        required=True,
		widget=forms.TextInput(attrs={
            'value': 'Dor de cabeça',
			'placeholder': 'Insira o nome da doença',
			'oninvalid': "this.setCustomValidity('Por favor insira o nome da doença aqui')"
		}))
    # description = forms.CharField(
	# 	max_length=255,
    #     required=False,
	# 	widget=forms.Textarea(attrs={
    #         'text': 'Aquece me todo o corpo e fico sem apetite',
	# 		'placeholder': 'Insira a descriçao da doença',
	# 		'oninvalid': "this.setCustomValidity('Por favor insira a descriçao da doença aqui')"
	# 	}))
    date = forms.CharField(
		max_length=255,
        required=True,
		widget=DateInput
    )
    priority = forms.ChoiceField(
        choices=PRIORITY,
        required=False,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )