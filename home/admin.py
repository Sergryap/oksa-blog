from django.contrib import admin
from .models import *


class CourseInline(admin.TabularInline):
	model = Course
	ordering = ['course_date']
	verbose_name = 'Курс'
	verbose_name_plural = 'Курсы'

# filter_horizontal = ['course_date']
# formset = CourseDataInlineFormset


class CourseStudentInline(admin.TabularInline):
	model = CourseStudent
	# ordering = ['course_date']
	verbose_name = 'Запись на курс'
	verbose_name_plural = 'Запись на курс'


class ProgramGalleryInline(admin.TabularInline):
	model = ProgramGallery
	verbose_name = 'Галерея'
	verbose_name_plural = 'Галерея'


class ProgramDetailInline(admin.TabularInline):
	model = ProgramDetail
	verbose_name = 'Блок'
	verbose_name_plural = 'Блоки'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	inlines = [CourseStudentInline]
	list_display = ['program', 'teacher', 'price', 'course_date']
	list_editable = ['course_date', 'price']
	list_filter = ['program', 'course_date']
	filter_horizontal = ['students']
	search_fields = ['program']
	ordering = ['course_date', 'program']
	prepopulated_fields = {'slug': ('program', 'course_date')}
	list_per_page = 5
	extra = 3


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
	inlines = [CourseInline, ProgramGalleryInline, ProgramDetailInline]
	list_display = ['name', 'description', 'image']
	list_editable = ['description', 'image']
	list_filter = ['name']
	search_fields = ['name']
	ordering = ['name']
	prepopulated_fields = {'slug': ('name',)}
	list_per_page = 5
	extra = 3


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	inlines = [CourseStudentInline]
	list_display = ['first_name', 'last_name', 'phone']
	list_filter = ['first_name', 'last_name']
	filter_horizontal = ['courses']
	extra = 3


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	inlines = [CourseInline]
	list_display = ['first_name', 'last_name', 'phone']
	list_filter = ['first_name', 'last_name']
	extra = 3


@admin.register(Motivation)
class MotivationAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'image']
	list_editable = ['description', 'image']
	list_filter = ['name']
	search_fields = ['name']
	ordering = ['name']
	list_per_page = 5
	extra = 3


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'image', 'image_latest_coures_inner']
	list_editable = ['description', 'image', 'image_latest_coures_inner']
	list_filter = ['name']
	ordering = ['name']
