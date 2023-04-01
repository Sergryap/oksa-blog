from django.db import models
from django.urls import reverse


class Program(models.Model):
	name = models.CharField(max_length=20, verbose_name='Наименование')
	description = models.TextField(verbose_name='Краткое описание')
	image = models.ImageField(upload_to='programs_images', null=True, blank=True, verbose_name='Изображение')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

	class Meta:
		verbose_name = 'Программа'
		verbose_name_plural = 'Программы'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('program_details', kwargs={'program_slug': self.slug})


class ProgramGallery(models.Model):
	image = models.ImageField(upload_to='program_gallery_images', null=True, blank=True, verbose_name='Изображение')
	program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='gallery', verbose_name='Галерея')


class ProgramDetail(models.Model):
	title = models.CharField(max_length=30, null=True, blank=True, verbose_name='Заголовок')
	detail = models.TextField(null=True, blank=True, verbose_name='Детальное описание')
	image = models.ImageField(upload_to='program_blok_images', null=True, blank=True, verbose_name='Изображение')
	program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='details', verbose_name='Блоки')


class Teacher(models.Model):
	first_name = models.CharField(max_length=30, default='Оксана', verbose_name='Имя')
	last_name = models.CharField(max_length=30, default='Ряпина', verbose_name='Фамилия')
	phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Телефон')
	social_profile = models.CharField(max_length=255, null=True, blank=True)
	programs = models.ManyToManyField(Program, related_name='teachers', through='Course')

	class Meta:
		verbose_name = 'Преподаватель'
		verbose_name_plural = 'Преподаватели'

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class Course(models.Model):
	program = models.ForeignKey(
		Program,
		on_delete=models.CASCADE,
		related_name='courses',
		verbose_name='Программа',
		null=True, blank=True)

	teacher = models.ForeignKey(
		Teacher,
		on_delete=models.CASCADE,
		related_name='courses',
		verbose_name='Преподаватель',
		null=True, blank=True)

	price = models.PositiveIntegerField(verbose_name='Цена')
	course_date = models.DateField(verbose_name="Дата курса", null=True, blank=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'
		ordering = ['course_date']

	def __str__(self):
		return f"{self.program.name}_{self.course_date}"


class Student(models.Model):
	first_name = models.CharField(max_length=30, verbose_name='Имя')
	last_name = models.CharField(max_length=30, verbose_name='Фамилия', null=True, blank=True)
	phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Телефон')
	social_profile = models.CharField(max_length=255, null=True, blank=True)
	courses = models.ManyToManyField(Course, related_name='students', verbose_name='Курсы', through='CourseStudent')

	class Meta:
		verbose_name = 'Студент'
		verbose_name_plural = 'Студенты'

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class CourseStudent(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_data', verbose_name='Студент')
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_data', verbose_name='Курс')
	Prepayment = models.PositiveIntegerField(verbose_name='Предоплата', null=True, blank=True)
	Note = models.CharField(max_length=500, verbose_name='Примечание', null=True, blank=True)

	class Meta:
		verbose_name = 'Запись на курс'
		verbose_name_plural = 'Запись на курс'

	def __str__(self):
		return f"{self.student}_{self.course}"


class Motivation(models.Model):
	name = models.CharField(max_length=100, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание')
	image = models.ImageField(upload_to='motivation_images', null=True, blank=True, verbose_name='Изображение')

	class Meta:
		verbose_name = 'Мотивация'
		verbose_name_plural = 'Мотивации'

	def __str__(self):
		return self.name


class Slider(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название')
	description = models.TextField(verbose_name='Описание', null=True, blank=True)
	image = models.ImageField(upload_to='slider_images', null=True, blank=True, verbose_name='Изображение')
	image_latest_coures_inner = models.ImageField(upload_to='slider_images', null=True, blank=True, verbose_name='Изображение_блока')

	class Meta:
		verbose_name = 'изображение'
		verbose_name_plural = 'Главная страница'

	def __str__(self):
		return self.name
