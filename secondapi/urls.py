from django.urls import path
from . import views

urlpatterns=[
    path('',views.Allstudent.as_view()),
    path('<int:student_id>/',views.Allstudent1.as_view())
]
