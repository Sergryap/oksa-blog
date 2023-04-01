from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import *
from datetime import datetime as dt

# ^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{2,3}[\s\-]?[0-9]{2,3}[\s\-]?[0-9]{2,3} регулярка проверки номера телефона


menu = {
	'В начало': ['home'],
	'Наши курсы': ['courses'],
	'Контакты': ['contact'],
	# 'Pages': {
	# 	'Event': 'event',
	# 	'Event-Details': 'event_details',
	# 	'Admissions': 'admissions',
	# 	'Elements': 'elements'},
	'Блог': ['blog']
}


def home(request):
	template = 'home/index.html'
	programs = Program.objects.all()
	motivations = Motivation.objects.all()
	slider = Slider.objects.all()
	course_actual = Course.objects.filter(course_date__gte=dt.now())[0]
	context = {
		'menu': menu,
		'programs': programs,
		'motivations': motivations,
		'slider': slider,
		'course_actual': course_actual,
		'marketing':
		f"""
		Курс, на ближайшее время.
		Чтобы записаться, заполните контактную форму
		либо свяжитесь с нами.
		"""
	}
	return render(request, template, context=context)


def courses(request):
	template = 'home/courses.html'
	programs = Program.objects.all()
	context = {'menu': menu, 'programs': programs}
	return render(request, template, context=context)


def contact(request):
	template = 'home/contact.html'
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			message = form.cleaned_data['message']
			name = form.cleaned_data['name']
			from_email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			try:
				send_mail(
					f'"{subject}" от {name} {from_email}',
					message,
					settings.EMAIL_HOST_USER,
					settings.RECIPIENTS_EMAIL
				)
			except BadHeaderError:
				return HttpResponse('Ошибка в теме письма.')
	else:
		form = ContactForm()
	context = {'form': form, 'menu': menu}
	return render(request, template, context=context)


def blog(request):
	# template = 'home/blog.html'
	# context = {'menu': menu}
	return redirect('https://oksa-studio.ru/blog/')


def single_blog(request):
	template = 'home/index.html'
	context = {'menu': menu}
	return render(request, template, context=context)


def event(request):
	template = 'home/index.html'
	context = {'menu': menu}
	return render(request, template, context=context)


def program_details(request, program_slug):
	template = 'home/program_details.html'
	program = get_object_or_404(Program, slug=program_slug)
	context = {'menu': menu, 'program': program}
	return render(request, template, context=context)


def admissions(request):
	template = 'home/index.html'
	context = {'menu': menu}
	return render(request, template, context=context)


def elements(request):
	template = 'home/index.html'
	context = {'menu': menu}
	return render(request, template, context=context)
