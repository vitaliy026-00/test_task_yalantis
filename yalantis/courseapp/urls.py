from django.urls import path
from . import views
urlpatterns = [
    path('', views.course, name = 'course_start'),
    path('course-<int:pk>', views.NewsView.as_view(), name='course-number'),
    path('create-course', views.course_create, name='create-course'),
    path('course-<int:pk>/delete', views.CourseDelete.as_view(), name='course-delete'),
    path('course-<int:pk>/update', views.CourseUpdate.as_view(), name='course-update'),

]