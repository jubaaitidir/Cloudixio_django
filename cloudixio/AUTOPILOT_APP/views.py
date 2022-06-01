
from django.views import generic
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from AUTOPILOT_APP.models import Consultant, Mission, TimeSheet, MissionsType, ActivitesType, ActivitesMissions


from .forms import FiltresActivitesMissions, FiltresTimeSheet, FormInscription, FormConnexion


def hello(request):
    consultants = Consultant.objects.all()
    return HttpResponse(f"""<h1>Hello Cloudixio<h1>
                        <h2>my favorite consultants: </h2>
                        <ul>
                        <li>identifiant : {consultants[0].idConsultant} Mr:{consultants[0].prenom} </li>
                        <li>identifiant : {consultants[1].idConsultant} Mr:{consultants[1].prenom}</li>
                        </ul>""")


def about(request):
    return HttpResponse("""<h1>About-us</h1>
                        CLOUDIXIO AIDE LES ORGANISATIONS À CROITRE, INNOVER, DÉVELOPPER LEURS CAPACITÉS, 
                        ET CRÉER DE NOUVEAUX BUSINESS<h2></h2>""")


class DetailConsltantTimesheets(generic.DetailView):
    model=Consultant
    template_name='AUTOPILOT_APP/filter/consultant_timesheets.html'



class ListConsultantView(generic.ListView):
    template_name ='AUTOPILOT_APP/list/list_consultants.html'
    context_object_name = 'consultants'
    def get_queryset(self):
        return Consultant.objects.all()



class ListMissionView(generic.ListView):
    template_name= 'AUTOPILOT_APP/list/list_missions.html'
    context_object_name= 'missions'
    
    def get_queryset(self):
        return Mission.objects.all()
        
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Liste des missions'
        return context

 


class ListTimesheetView(generic.ListView):
    template_name= 'AUTOPILOT_APP/list/list_timesheets.html'
    context_object_name= 'timesheets'
 
    def get_queryset(self):
        return TimeSheet.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Liste de Timesheets'
        context['form'] = FiltresTimeSheet()
        return context


class ListMissionTypeView(generic.ListView):
    template_name= 'AUTOPILOT_APP/list/list_missionsType.html'
    context_object_name= 'missionsType'
    
    def get_queryset(self):
        return MissionsType.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Liste de types missions'
        return context


class ListActivitesTypeView(generic.ListView):
    template_name= 'AUTOPILOT_APP/list/list_activitesType.html'
    context_object_name= 'activitesType'
    
    def get_queryset(self):
        return ActivitesType.objects.all()
        
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Liste des types d\'activites'
        return context
    
class ListActivitesMissionsView(generic.ListView):
    template_name= 'AUTOPILOT_APP/list/list_activitesMissions.html'
    context_object_name= 'activitesMissions'
    
    def get_queryset(self):
        return ActivitesMissions.objects.all()
        
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Liste des activites missions'
        context['consultants']= FiltresActivitesMissions()
        return context




class DetailConsultantView(generic.DetailView):
    model= Consultant
    template_name= 'AUTOPILOT_APP/detail/consultant_detail.html'
    
    
class DetailMissionView(generic.DetailView):
    model= Mission
    template_name='AUTOPILOT_APP/detail/mission_detail.html'
    
    
class DetailTimesheetView(generic.DetailView):
    model=TimeSheet
    template_name='AUTOPILOT_APP/detail/timesheet_detail.html'


class DetailTypeMissionView(generic.DetailView):
    model = MissionsType
    template_name='AUTOPILOT_APP/detail/missionType_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Détail type mission'
        return context
  
class DetailActiviteTypeView(generic.DetailView):
    model = ActivitesType
    template_name='AUTOPILOT_APP/detail/activiteType_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Détail type activité'
        return context



def inscription(request):
    if request.method == "POST":
        form = FormInscription(request.POST)
        context = {
            'form': form,
            'message': 'Inscription',
            'error':'',
            'register':''
        }

        if form.is_valid():
            if(Consultant.objects.filter(email=form.cleaned_data['email'])):
                context.update({'error':'Ce nom d\'utilisateur existe!'})
            else:
                if(form.save()):
                    context.update({'register':'OK'})
                    return HttpResponseRedirect('/connexion/')
                else:
                    context.update({'error':'inscription échouée veuillez réessayer !','register':'KO'})
    else:

        form = FormInscription()
        context = {
            'form': form,
            'message': 'Inscription',
            'error':''
        }
    return render(request, 'AUTOPILOT_APP/account/inscription.html', {"context": context})


def connexion(request):

    if request.method == "POST":
        form = FormConnexion(request.POST)
        context = {
            'form': form,
            'message': 'Connexion',
            'error': ''
        }
        if form.is_valid():
            if(Consultant.objects.filter(email=form.cleaned_data['email'])):
                consultant = Consultant.objects.get(email=form.cleaned_data['email'])

                if(consultant.password == form.cleaned_data['password']):
                    url = "/"+str(consultant.idConsultant) + "/profil/"
                    return HttpResponseRedirect(url)
                else:
                    context.update({'error': "mot de passe incorrecte"})

            else:
                context.update({'error': "Cette adresse email n'existe pas!"})

    else:

        form = FormConnexion()
        context = {
            'form': form,
            'message': 'Connexion',
            'error': ''
        }

    return render(request, 'AUTOPILOT_APP/account/connexion.html', {"context": context})


class ProfilView(generic.DetailView):
    model=Consultant
    template_name="AUTOPILOT_APP/account/profil.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titre'] = 'Profil du consultant'
        return context
    
    
    
   