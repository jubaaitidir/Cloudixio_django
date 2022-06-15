from types import AsyncGeneratorType
from django import forms
from .models import ActivitesMissions, ActivitesType, Competences, Consultant, Mission, TimeSheet

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
        
        
#----------------------------------------------------
# Les form de Filtres
#----------------------------------------------------
class FiltresConsultant(forms.ModelForm): 
    idConsultant = forms.ModelChoiceField(Consultant.objects.all().values_list('idConsultant', flat=True).distinct(), empty_label="Id Consulant", widget = forms.Select(attrs = {'onchange' : "filter(this.value);"}))
    # nom = forms.ModelChoiceField(Consultant.objects.all().values_list('nom', flat=True).distinct(), empty_label="Nom",widget = forms.Select(attrs = {'onchange' : "filter(this.value);"}))
    # prenom=forms.ModelChoiceField(Consultant.objects.all().values_list('prenom', flat=True).distinct(), empty_label="Prénom")
    # competence=forms.ModelChoiceField(Competences.objects.all().values_list('description', flat=True).distinct(), empty_label="Compétence",widget = forms.Select(attrs = {'onchange' : "filter(this.value);"}))
    def __init__(self, *args, **kwargs):
        super(FiltresConsultant, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            # field.widget.attrs['placeholder'] = field.label
            field.label = ''
    class Meta:
        model= Consultant
        fields=['idConsultant']
# FiltresConsultant().as_ul()




class FiltresTimeSheet(forms.Form): 
    idMission = forms.ModelChoiceField(Mission.objects.filter(idMission__in=(TimeSheet.objects.all().values_list('idMission',flat=True).distinct())).values_list('nomMission',flat=True), empty_label="Mission")
    idConsultant = forms.ModelChoiceField(Consultant.objects.filter(idConsultant__in=(TimeSheet.objects.all().values_list('idConsultant',flat=True).distinct())).values_list('nom',flat=True), empty_label="Consulant")
    annee=forms.ModelChoiceField(TimeSheet.objects.all().values_list('annee', flat=True).distinct(), empty_label="Annee")
    semaine=forms.ModelChoiceField(TimeSheet.objects.all().values_list('semaine', flat=True).distinct(), empty_label="Semaine")
    tempsPasse=forms.ModelChoiceField(TimeSheet.objects.all().values_list('tempsPasse', flat=True).distinct(), empty_label="Temps passé")
    def __init__(self, *args, **kwargs):
        super(FiltresTimeSheet, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            # field.widget.attrs['placeholder'] = field.label
            field.label = ''
FiltresTimeSheet().as_ul()

class FiltresActivitesMissions(forms.Form): 
    idActivitesType = forms.ModelChoiceField(ActivitesType.objects.filter(idActivitesType__in=(ActivitesMissions.objects.all().values_list('idActivitesType',flat=True).distinct())).values_list('description',flat=True), empty_label="Mission")
    idMission = forms.ModelChoiceField(Mission.objects.filter(idMission__in=(ActivitesMissions.objects.all().values_list('idMission',flat=True).distinct())).values_list('nomMission',flat=True), empty_label="Mission")
    idConsultant = forms.ModelChoiceField(Consultant.objects.filter(idConsultant__in=(ActivitesMissions.objects.all().values_list('idConsultant',flat=True).distinct())).values_list('nom',flat=True), empty_label="Consulant")
    tjm=forms.ModelChoiceField(ActivitesMissions.objects.all().values_list('tjm', flat=True).distinct(), empty_label="TJM")
    estimationCharge=forms.ModelChoiceField(ActivitesMissions.objects.all().values_list('estimationCharge', flat=True).distinct(), empty_label="Estimation Charge")
    def __init__(self, *args, **kwargs):
        super(FiltresActivitesMissions, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            # field.widget.attrs['placeholder'] = field.label
            field.label = ''
FiltresTimeSheet().as_ul()

