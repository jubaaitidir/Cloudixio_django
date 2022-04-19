# from msilib.schema import Class
from django.db import models
import datetime

class Consultant(models.Model):
    idConsultant = models.fields.BigAutoField(primary_key=True,null=False)
    nom = models.fields.CharField(max_length=100, default='NULL')
    prenom = models.fields.CharField(max_length=100, default='NULL')


class Mission(models.Model):
    idMission= models.fields.BigAutoField(primary_key=True, null=False)
    # idMissionType= models.ForeignKey(MissionType, null=True,on_delete=models.SET_NULL)
    startDate= models.fields.DateField(null=False)
    endDate = models.fields.DateField()
    nomMission= models.fields.TextField(null=False)
    
    
class TimeSheet(models.Model):
    idTimeSheet = models.fields.BigAutoField(primary_key=True, null=False)
    idMission = models.ForeignKey(Mission, null=True, on_delete=models.SET_NULL)
    idConsultant = models.ForeignKey(Consultant, null=True, on_delete=models.SET_NULL)
    annee = models.fields.SmallIntegerField(choices=[(r,r) for r in range(2000, datetime.date.today().year)])
    semaine = models.fields.SmallIntegerField(choices=[(r,r) for r in range(1,53)])
    

