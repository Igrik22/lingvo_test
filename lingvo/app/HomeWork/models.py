from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from HomeWork.validators import validate_file_size

User = get_user_model()

faculty_choices = [
        ('B', 'Business'),
        ('M', 'Medicine'),
        ('I', 'IT'),
    ]


class Work(models.Model):

    faculty = models.CharField(max_length=2, choices=faculty_choices, default='B')

    class Meta:
        abstract = True


class HomeWork(Work):  # HomeWork
    title = models.CharField(max_length=4096)
    work_text = models.TextField(verbose_name='Work_text')
    home_work_file = models.FileField(upload_to='Home-work/')
    comment = models.TextField(verbose_name='Comments')
    pub_date = models.DateTimeField('Date_published', auto_now_add=True)
    finished_date = models.DateTimeField('Finished_date', auto_now_add=False)

    def __str__(self):
        return self.title


class FinishedHomeWork(Work):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=4096, default=None)
    home_work = models.ForeignKey(HomeWork, verbose_name='Home_work', on_delete=models.CASCADE)
    finished_home_work_file = models.FileField\
        (upload_to='Finished-home-work/', validators=[validate_file_size, FileExtensionValidator(['txt'])])
    created = models.DateTimeField(auto_now=True)
    mark = models.PositiveSmallIntegerField(verbose_name='Mark', null=True, blank=True,
                                            validators=[MinValueValidator(0), MaxValueValidator(10)])
    comment_of_mark = models.TextField(verbose_name='comment_of_mark', null=True, blank=True)

    def __str__(self):
        return self.title


