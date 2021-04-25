from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import Course
from .serializer import CourseSer
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import CourseForm
from django.db.models import Q
def course(request):
    search_form = request.GET.get('search', '')
    if search_form:
        post = Course.objects.filter(Q(name__icontains=search_form)).order_by('date_start')
    else:
        post = Course.objects.all().order_by('date_start')
    data = {
        'post': post,
    }
    return render(request, 'courseapp/course_1.html', data)
def template(request):
    return render(request, 'courseapp/template.html')

class NewsView(DetailView):
    model = Course
    template_name = 'courseapp/course_view.html'
    context_object_name = 'course'
def course_create(request):

    error = ''
    if request.method == 'POST':

        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_start')
        else:
            error = 'Щось не так'


    form = CourseForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'courseapp/course_create.html', data)
class NewsUpdate(UpdateView):
    model = Course
    template_name = 'courseapp/course-update.html'
    form_class = CourseForm

class CourseDelete(DeleteView):
    model = Course
    template_name = 'courseapp/course_delete.html'
    form_class = CourseForm
    success_url = '/'
class CourseUpdate(UpdateView):
    model = Course
    template_name = 'courseapp/course_update.html'
    form_class = CourseForm
    success_url = '/'