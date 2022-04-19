from django.shortcuts import render
from django.http import HttpResponse

from AUTOPILOT_APP.models import Consultant

def hello(request):
    consultants= Consultant.objects.all()
    return HttpResponse(f"""<h1>Hello Cloudixio<h1>
                        <h2>my favorite consultants: </h2>
                        <ul>
                        <li>identifiant : {consultants[0].idConsultant} Mr:{consultants[0].prenom} </li>
                        <li>identifiant : {consultants[1].idConsultant} Mr:{consultants[1].prenom}</li>
                        </ul>""")

def about(request):
    return HttpResponse("""<h1>About-us</h1>
                        CLOUDIXIO AIDE LES ORGANISATIONS À CROITRE, INNOVER, DÉVELOPPER LEURS CAPACITÉS, ET CRÉER DE NOUVEAUX BUSINESS<h2></h2>""")