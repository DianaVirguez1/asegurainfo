from django.db import models
from datetime import datetime

from django.forms import model_to_dict

class Norma (models.Model):
     id_nor_pk = models.AutoField(primary_key=True)
     nor = models.CharField(verbose_name='Nombre', max_length=60)
     des_nor = models.CharField(verbose_name='Descripción', max_length=200)
     
    
     def __str__(self) -> str:
          return self.nor
      
     def toJSON(self):
        item = model_to_dict(self)
        return item

     class Meta:
        verbose_name = 'Norma'
        verbose_name_plural = 'Normas'
        ordering = ['id_nor_pk']
     
class Punto (models.Model):
     id_pun_pk = models.AutoField(primary_key= True)
     num_pun = models.IntegerField(verbose_name="Numeral")
     nomb_pun = models.CharField (verbose_name= "Nombre",max_length=60)
     norma = models.ForeignKey(Norma, on_delete=models.CASCADE, verbose_name='Norma')

     def __str__(self) -> str:
         return self.nomb_pun
     def toJSON(self):
        item = model_to_dict(self)  
        item['norma'] = self.norma.toJSON()   
        return item

     class Meta:
        verbose_name = 'Punto'
        verbose_name_plural = 'Puntos'
        ordering = ['id_pun_pk']
     
class Item (models.Model):
     id_item_pk = models.AutoField(primary_key= True)
     num_item = models.FloatField(verbose_name="Numeral")
     nomb_item = models.CharField (max_length=120, verbose_name="Nombre Item")
     punto = models.ForeignKey(Punto, on_delete=models.CASCADE)

     def __str__(self) -> str:
         return  self.nomb_item
     
     def toJSON(self):
        item = model_to_dict(self)
        return item

     class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['id_item_pk']
     
class Requisito (models.Model):
     id_req_pk = models.AutoField(primary_key= True)
     nomb_req  = models.CharField(max_length=5, verbose_name="Nombre")
     descrip_req = models.TextField(max_length=255, verbose_name="Descripción")
     nota_req = models.CharField(max_length=255, verbose_name="Nota")
     infdoc_req = models.CharField(max_length=255,verbose_name="Información Documentada")
     cambios_req = models.CharField(max_length=255,verbose_name="Cambios")
     infdoc_exist_req = models.CharField(max_length=255,verbose_name="Informacion Doc Existente")
     infdoc_falta_req = models.CharField (max_length=255,verbose_name="Informacion Doc Faltante")
     esqcumplact_req = models.CharField (max_length=255,verbose_name="Esquema Cumplimiento Actual")
     infdoc_elab_req = models.CharField (max_length=255,verbose_name="Información Doc a Elaborar")
     actrealizar_req = models.CharField (max_length=255,verbose_name="Información Doc a Elaborar")
     item =  models.ForeignKey(Item, on_delete=models.CASCADE)

     def __str__(self) -> str:
         return  self.nomb_req
     
     def toJSON(self):
        requisito = model_to_dict(self)
        return requisito

     class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'
        ordering = ['id_req_pk']
    
class Empresa (models.Model):
     id_emp_pk = models.AutoField(primary_key= True)
     nomb_empresa  = models.CharField(max_length=150, verbose_name="Nombre Empresa")
     raz_empresa  = models.CharField(max_length=250, verbose_name="Razón Social Empresa")
     nit_empresa = models.CharField(max_length=15, verbose_name="Nit Empresa")

     def _str_(self) -> str:
         return  self.nomb_empresa
     
     def toJSON(self):
        empresa = model_to_dict(self)
        return empresa

     class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['id_emp_pk']
    
    
class Evaluacion (models.Model):
     id_eva_pk = models.AutoField(primary_key= True)
     eva_descripcion  = models.CharField(max_length=5, verbose_name="Evaluación Descripción")
     eva_calificacion  = models.IntegerField(verbose_name="Numeral")
     eva_criterio  = models.CharField(max_length=5, verbose_name="Evaluación Criterio")

     def _strc_(self) -> str:
         return  self.eva_descripcion
     
     
    

class EvaReqEmpresa (models.Model):
     id_eva_req_emp_pk = models.AutoField(primary_key= True)
     requisito = models.ForeignKey(Requisito, on_delete=models.CASCADE)
     empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
     evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)