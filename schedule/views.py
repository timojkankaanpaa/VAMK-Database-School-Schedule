from django.views import generic
from .models import Course, Curriculum, Room, Group, Teacher
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CourseView(generic.ListView):
	template_name = 'schedule/course.html'
	context_object_name = 'all_courses'

	def get_queryset(self):
		return Course.objects.all()

class CourseDetail(generic.DetailView):
	model = Course
	template_name = 'schedule/course_detail.html'

class CourseCreate(CreateView):
	model = Course
	fields = ['code', 'language', 'name', 'credit', 'semester', 'curriculumid']

class CurriculumView(generic.ListView):
	template_name = 'schedule/curriculum.html'
	context_object_name = 'all_curriculums'

	def get_queryset(self):
		return Curriculum.objects.all()

class CurriculumDetail(generic.DetailView):
	model = Curriculum
	template_name = 'schedule/curriculum_detail.html'

class CurriculumCreate(CreateView):
	model = Curriculum
	fields = ['name']

class RoomView(generic.ListView):
	template_name = 'schedule/room.html'
	context_object_name = 'all_rooms'

	def get_queryset(self):
		return Room.objects.all()

class RoomDetail(generic.DetailView):
	model = Room
	template_name = 'schedule/room_detail.html'
	
class RoomCreate(CreateView):
	model = Room
	fields = ['name', 'seat']

class GroupView(generic.ListView):
	template_name = 'schedule/group.html'
	context_object_name = 'all_groups'

	def get_queryset(self):
		return Group.objects.all()

class GroupDetail(generic.DetailView):
	model = Group
	template_name = 'schedule/group_detail.html'
	
class GroupCreate(CreateView):
	model = Group
	fields = ['code', 'degree', 'curriculumid']

class TeacherView(generic.ListView):
	template_name = 'schedule/teacher.html'
	context_object_name = 'all_teachers'

	def get_queryset(self):
		return Teacher.objects.all()

class TeacherDetail(generic.DetailView):
	model = Teacher
	template_name = 'schedule/teacher_detail.html'

class TeacherCreate(CreateView):
	model = Teacher
	fields = ['code', 'name']