from django.db import models

# Create your models here.
class ConsumerUser(models.Model):
    id = f'K{models.AutoField(primary_key = True)}'
    consumer_email = models.CharField(max_length=255)
    consumer_password = models.CharField(max_length=64)
    consumer_full_name = models.CharField(max_length=100)
    consumer_telp = models.CharField(max_length=15)

    sex_choices = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan')
    )
    consumer_sex = models.CharField(
        max_length=1,
        choices=sex_choices,
        default='L'
    )

    consumer_birth_date = models.DateField()
    consumer_address = models.TextField()

    def __str__(self):
        return f'({self.id})'
