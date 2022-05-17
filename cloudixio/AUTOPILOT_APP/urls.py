from django.urls import path
from . import views

app_name='autopilot_app'
urlpatterns=[
    # path('',views.hello,name='index'),
    # path('<int:pk>', views.DetailView.as_view(), name='consultant'),
    # path('<int:pk>/results', views.ResultsView.as_view(), name='mission'),
    path('consultants/', views.consultant, name='consultant'),
    path('<int:consultant_id>/consultant', views.detail, name='detail'),
    path('<int:mission_id>/mission', views.mission, name='mission'),
    path('<int:timesheet_id>/timesheet', views.timeSheet, name='timesheet'),
]
