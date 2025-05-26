from django.db import models

# Create your models here.
class  Historial(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=100)
    actividad=models.CharField(max_length=210)
    fecha=models.DateField()
    resultado=models.TextField()

    def __str__(self):
        fila= "{0}: {1} {2}"
        return fila.format(self.id,self.usuario,self.actividad,self.fecha,self.resultado)
    
