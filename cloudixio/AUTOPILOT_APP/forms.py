from types import AsyncGeneratorType
from django import forms

from .models import ActivitesMissions, ActivitesType, Consultant, Mission, TimeSheet

class FormInscription(forms.ModelForm):
    nom= forms.CharField(label="Nom")
    prenom= forms.CharField(label="prenom")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe")
    class Meta:
        model= Consultant
        fields=['nom','prenom','email','password']

class FormConnexion(forms.ModelForm):
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'Jhon@address.com'}))
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'placeholder': 'Votre mot de passe ...'}))
    class Meta:
        model= Consultant
        fields=['email','password']
        
class FiltresTimeSheet(forms.Form): 
    idMission = forms.ModelChoiceField(Mission.objects.filter(idMission__in=(TimeSheet.objects.all().values_list('idMission',flat=True).distinct())).values_list('nomMission',flat=True), empty_label="Mission")
    idConsultant = forms.ModelChoiceField(Consultant.objects.filter(idConsultant__in=(TimeSheet.objects.all().values_list('idConsultant',flat=True).distinct())).values_list('nom',flat=True), empty_label="Consulant")
    annee=forms.ModelChoiceField(TimeSheet.objects.all().values_list('annee', flat=True).distinct(), empty_label="Annee")
    semaine=forms.ModelChoiceField(TimeSheet.objects.all().values_list('semaine', flat=True).distinct(), empty_label="Semaine")
    tempsPasse=forms.ModelChoiceField(TimeSheet.objects.all().values_list('tempsPasse', flat=True).distinct(), empty_label="Temps passé")
   
FiltresTimeSheet().as_ul()

class FiltresActivitesMissions(forms.Form): 
    idActivitesType = forms.ModelChoiceField(ActivitesType.objects.filter(idActivitesType__in=(ActivitesMissions.objects.all().values_list('idActivitesType',flat=True).distinct())).values_list('description',flat=True), empty_label="Mission")
    idMission = forms.ModelChoiceField(Mission.objects.filter(idMission__in=(ActivitesMissions.objects.all().values_list('idMission',flat=True).distinct())).values_list('nomMission',flat=True), empty_label="Mission")
    idConsultant = forms.ModelChoiceField(Consultant.objects.filter(idConsultant__in=(ActivitesMissions.objects.all().values_list('idConsultant',flat=True).distinct())).values_list('nom',flat=True), empty_label="Consulant")
    tjm=forms.ModelChoiceField(ActivitesMissions.objects.all().values_list('tjm', flat=True).distinct(), empty_label="TJM")
    estimationCharge=forms.ModelChoiceField(ActivitesMissions.objects.all().values_list('estimationCharge', flat=True).distinct(), empty_label="Estimation Charge")
 
FiltresTimeSheet().as_ul()