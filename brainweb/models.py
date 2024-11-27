from django.db import models 
from django.db.models import Model 
from django.core.exceptions import ValidationError
import brainweb.webhelper as helper

CNPJ_LENGTH = 14

class Crop(models.Model): 
    name = models.CharField(max_length=50, 
        verbose_name='Cultura',
        blank=False, 
        unique=True)

    def __str__(self):
        return str(self.name)

def validate_cpf_cnpj(value):
    if len(value)<CNPJ_LENGTH:
        validation = helper.validate_cpf(value)
    else:
        validation = helper.validate_cnpj(value)

    if not validation:
        raise ValidationError("CPF/CNPJ Inválido!")

class RuralProducer(models.Model):
    documentId = models.CharField(unique=True, 
                                  max_length = CNPJ_LENGTH,
                                  validators =[validate_cpf_cnpj],
                                  null=False, 
                                  verbose_name='CPF/CNPJ')
    producerName = models.CharField(max_length = 50,
                                  null=False, 
                                  verbose_name='Nome do Produtor')
    producerFarm = models.CharField(max_length = 50,
                                  null=False, 
                                  verbose_name='Nome da Fazenda')
    city = models.CharField(max_length = 60,
                                  null=False, 
                                  verbose_name='Cidade')
    state = models.CharField(max_length = 2,
                                  null=False, 
                                  verbose_name='Estado')
    totalArea = models.DecimalField(max_digits=11, 
                                    decimal_places=2, 
                                    default=0.00,
                                    null=False, 
                                    blank=False,
                                    verbose_name='Área Total(ha)')
    plantingArea = models.DecimalField(max_digits=11, 
                                       decimal_places=2, 
                                       default=0.00,
                                       null=False, 
                                       blank=False,
                                       verbose_name='Área Agricultável(ha)')
    preservationArea = models.DecimalField(max_digits=11, 
                                           decimal_places=2, 
                                           default=0.00,
                                           null=False, 
                                           blank=False,
                                           verbose_name='Área Vegetação(ha)')
    crops = models.ManyToManyField(Crop,
	verbose_name='Culturas'
    )

    def clean(self):
        errors={}
        if (self.plantingArea + self.preservationArea) > self.totalArea:
            errors['totalArea']= ('A soma das áreas Agrícultável e Vegetação não pode ultrapassar a área total!')
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.producerName

