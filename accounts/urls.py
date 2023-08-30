from django.urls import path
from .views import *

urlpatterns = [
    path('company_register/', CompanyRegisterView.as_view()),
    path('applicant_register/', ApplicantProfileView.as_view()),


]