from django.urls import path
from . import views

app_name='autopilot_app'
urlpatterns=[
    # path('',views.hello,name='index'),
    # path('<int:pk>', views.DetailView.as_view(), name='consultant'),
    # path('<int:pk>/results', views.ResultsView.as_view(), name='mission'),
    
    #Lists URLS
    path('consultants/', views.ListConsultantView.as_view(), name='consultants'),
    path('missions/', views.ListMissionView.as_view(), name='missions'),
    path('timesheets/', views.ListTimesheetView.as_view(), name='timesheets'),
    path('missionsType/', views.ListMissionTypeView.as_view(), name='missionsType'),
    path('activitesType/', views.ListActivitesTypeView.as_view(), name='missionsType'),
    path('activitesMissions/', views.ListActivitesMissionsView.as_view(), name='activitesMissions'),
    
    #Detail URLS
    path('<int:pk>/consultantTimesheets', views.DetailConsltantTimesheets.as_view(), name='consultantTimesheets'),
    path('<int:pk>/consultant', views.DetailConsultantView.as_view(), name='consultant_detail'),
    path('<int:pk>/mission', views.DetailMissionView.as_view(), name='mission_detail'),
    path('<int:pk>/timesheet', views.DetailTimesheetView.as_view(), name='timesheet_detail'),
    path('<int:pk>/missionType', views.DetailTypeMissionView.as_view(), name='missionType_detail'),
    path('<int:pk>/activiteType', views.DetailActiviteTypeView.as_view(), name='activiteType_detail'),

   
    #Account urls
    path('<int:pk>/profil/', views.ProfilView.as_view(), name='profil'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
]
