from datetime import datetime

from django.utils.timezone import now

from django.db import models

# Create your models here.
from user.models import NewUser


class Exams(models.Model):
    Subjects = (
        ('1', 'İnformasiya təhlükəsizliyinin əsasları'),
        ('2', 'Verilənlər bazası'),
        ('3', 'Korporativ informasiya sistemləri'),
        ('4', 'İnsidentlərin idarə olunması'),
        ('5', 'İnformasiya təhlükəsizliyində süni intellekt'),
    )

    subject_name = models.CharField(choices=Subjects, max_length=100, verbose_name="Fənnin adı")
    result = models.IntegerField(default=0, verbose_name="İmtahanın nəticəsi")
    start_date = models.DateTimeField(verbose_name="Başlama tarixi", default=datetime.now)
    last_date = models.DateTimeField(verbose_name='Bitmə tarixi', default=datetime.now)
    participant_name = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=None, verbose_name="İştirakçı adı")
