from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length = 128)
    surname = models.CharField(max_length = 128)

    phone = models.CharField(max_length = 128)

    applied_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    def row(self) -> list:
        return [self.name, self.surname, self.phone, self.applied_at]