from django.db import models

class ChitRegistration(models.Model):
    CHITTYPES = [
        ('MCF', 'MCF'),
        ('MCD2', 'MCD2'),
        ('MCD4', 'MCD4'),
    ]
    
    chit_Type = models.CharField(max_length=4, choices=CHITTYPES)
    chit_Number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    address = models.TextField()
    num_Of_Chits = models.IntegerField()

    def __str__(self):
        return f"{self.chit_Type} - {self.chit_Number} - {self.name}"