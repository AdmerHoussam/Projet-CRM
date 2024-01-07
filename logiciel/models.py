from django.db import models

class Record(models.Model):
    creer = models.DateTimeField(auto_now_add = True)
    prenom = models.CharField(max_length = 40)
    nom = models.CharField(max_length = 40)
    email = models.CharField(max_length = 80)
    num_tel = models.CharField(max_length = 18)
    adresse = models.CharField(max_length = 40)
    ville = models.CharField(max_length = 40)
    departement = models.CharField(max_length = 40)
    code_postal = models.CharField(max_length = 10)
    
    def __str__(self):
        return(f"{self.prenom} {self.nom}")