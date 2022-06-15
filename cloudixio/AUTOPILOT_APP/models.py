# from msilib.schema import Class


from django.db import models
import datetime

class Competences(models.Model):
    idCompetence = models.AutoField(db_column='idCompetence', primary_key=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competences'

    def __str__(self):
        return self.description
    
class Consultant(models.Model):
    idConsultant = models.fields.BigAutoField(primary_key=True,null=False)
    nom = models.fields.CharField(max_length=100, default='NULL')
    prenom = models.fields.CharField(max_length=100, default='NULL')
    # email= models.fields.EmailField(default='')
    # password= models.fields.CharField(max_length=100)
    competences= models.ManyToManyField(Competences, through="ConsultantsCompetences")
    class Meta:
        managed = False
        db_table = 'consultant'
    def __str__(self):
        return str(self.prenom+" "+self.nom)



    
class ConsultantsCompetences(models.Model):
    idConsultantsCompetences = models.AutoField(blank=True, primary_key=True)
    idCompetence = models.ForeignKey(Competences, models.DO_NOTHING, db_column='idCompetence')  # Field name made lowercase.
    idConsultant = models.ForeignKey(Consultant, models.DO_NOTHING, db_column='idConsultant')  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'consultantsCompetences'



class MissionsType(models.Model):
    idMissionType = models.fields.BigAutoField(primary_key=True, null=False, db_column='idMissionType')
    titre= models.fields.TextField(blank=True, null=True, max_length=50)
    description=models.fields.TextField(blank=True, null=True, max_length=50)
    
    class Meta:
        managed = False
        db_table = 'missionsType'
    
    def __str__(self):
        return str(self.titre)


class Mission(models.Model):
    idMission= models.fields.BigAutoField(primary_key=True, null=False)
    idMissionType= models.ForeignKey(MissionsType, null=True,on_delete=models.SET_NULL,db_column='idMissionType')
    startDate= models.fields.DateField(null=False)
    endDate = models.fields.DateField()
    nomMission= models.fields.TextField(null=False)
    
    class Meta:
        managed = False
        db_table = 'missions'
        
    def __str__(self):
        return str(self.nomMission)




class TimeSheet(models.Model):
    idTimeSheet = models.fields.BigAutoField(primary_key=True, null=False)
    idMission = models.ForeignKey(Mission, null=True, on_delete=models.SET_NULL, db_column='idMission')
    idConsultant = models.ForeignKey(Consultant, null=True, on_delete=models.SET_NULL, db_column='idConsultant')
    annee = models.fields.SmallIntegerField(choices=[(r,r) for r in range(2000, datetime.date.today().year+30)])
    semaine = models.fields.SmallIntegerField(choices=[(r,r) for r in range(1,53)])
    tempsPasse = models.FloatField(db_column='tempsPassé', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timeSheet'

    def __str__(self):
        strIdTimesheet = str(self.idTimeSheet)
        return strIdTimesheet 


class ActivitesType(models.Model):
    idActivitesType = models.AutoField(db_column='idActivitesType', primary_key=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activitesType'

    def __str__(self):
        return self.description
    

class ActivitesMissions(models.Model):
    idActivitesMissions = models.AutoField(db_column='idActivitesMissions', primary_key=True)  # Field name made lowercase.
    idActivitesType = models.ForeignKey('Activitestype',models.DO_NOTHING,db_column='idActivitesType')  # Field name made lowercase.
    idMission = models.ForeignKey('Mission', models.DO_NOTHING, db_column='idMission')  # Field name made lowercase.
    idConsultant = models.ForeignKey('Consultant', models.DO_NOTHING, db_column='idConsultant')  # Field name made lowercase.
    tjm = models.FloatField(blank=True, null=True)
    estimationCharge = models.FloatField(db_column='estimationCharge', blank=True, null=True)  # Field name made lowercase.
    # devise = models.TextField(blank=True, null=True)
    # tauxchangeeur = models.FloatField(db_column='tauxChangeEur', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activitesMissions'
        # ordering = ['idConsultant']

