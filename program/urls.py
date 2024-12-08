from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.ProgramList.as_view()),
    # path("<int:pk>/", views.single_program_page),
    path("<int:pk>/", views.ProgramDetail.as_view()),
]