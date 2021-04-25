from .models import Course
from django.forms import ModelForm, TextInput, DateInput, Textarea

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'count_of_lc', 'date_start', 'date_end']
        widgets={
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of Course'

            }),
            'count_of_lc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Count of lectures'

            }),
            'date_start': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of start',

            }),
            'date_end': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of end',


            }),

        }