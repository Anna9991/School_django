from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Teacher(models.Model):
    TITLE_TYPES = [('t', "Teacher"), ('s', "Super Teacher")]

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, choices=TITLE_TYPES, default='t')
    instagram_url = models.URLField(max_length=200)
    photo = models.ImageField(upload_to='teachers_photos/')


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_lessons')
    photo = models.ImageField(upload_to='lesson_photos/')


class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()


class SchoolInfo(models.Model):
    foundation_year = models.IntegerField()
    number_of_students = models.IntegerField(default=0)
    number_of_awards = models.IntegerField(default=0)

    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    facebook_url = models.URLField(max_length=200)
    instagram_url = models.URLField(max_length=200)
    youtube_url = models.URLField(max_length=200)
    
    def years_since_foundation(self):
        current_year = timezone.now().year
        if self.foundation_year:
            return current_year - self.foundation_year
        return None
    
    def number_of_teachers(self):
        return Teacher.objects.count()
    
    def save(self, *args, **kwargs):
        if SchoolInfo.objects.exists() and not self.pk:
            raise ValidationError("Вы можете создать только одну запись для контактной информации.")
        super().save(*args, **kwargs)


class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    stars = models.IntegerField(default=0)