from django.db import models

class Course(models.Model):
    name = models.CharField('Name', max_length=255, null=False)
    count_of_lc = models.IntegerField('Count of lectures', null=False)
    date_start = models.DateField("Date of start", null=False)
    date_end = models.DateField("Date of end", null=False)

    def __str__(self):
        return f"{self.name},  {self.date_start}, {self.date_end}, {self.count_of_lc}"

    def get_absolute_url(self):
        return f'/-{self.id}'

    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'