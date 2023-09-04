from django.urls import path
from .views import *

urlpatterns = [
    path("job_add/",JobAddView.as_view()),

]