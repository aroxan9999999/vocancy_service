from django.db import models
from app.scripts import translite



class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="название насиленего пункта", unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'название населеного пункта'
        verbose_name_plural = 'название населенных пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translite(self.name)
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name="Язык програмирования", unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык програмирования'
        verbose_name_plural = 'Языки програмирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translite(str(self.name))
        super().save(*args, **kwargs)


class Vocancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=150, verbose_name="Загаловок")
    company = models.CharField(max_length=250, verbose_name="Компания")
    description = models.TextField(verbose_name="Описание")
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name="Город", blank=True, null=True)
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    timer = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Ваканчии"


class Error(models.Model):
    time = models.DateField(auto_now_add=True)




