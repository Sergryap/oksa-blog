from django import forms


class ContactForm(forms.Form):

	message = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': "form-control w-100",
				'cols': 30,
				'rows': 9,
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder = 'Введите сообщение'",
				'placeholder': "Сообщение"
			}),
		max_length=500, label='Сообщение')

	name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': "form-control valid",
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder = 'Введите ваше имя'",
				'placeholder': "Ваше имя"
			}),
		max_length=100, label='Ваше имя')

	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				'class': "form-control valid",
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder = 'Введите Email'",
				'placeholder': "Email"
			}),
		label='Email', required=False)

	subject = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': "form-control",
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder = 'Введите тему'",
				'placeholder': "Тема"
			}),
		max_length=50, label='Тема', required=False)
