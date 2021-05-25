from django.urls import path

from . import views

urlpatterns=[
     path('alportal',views.AlPortal, name='AlPortal'),
     path('stportal',views.StPortal, name='StPortal'),
     path('offers',views.offers, name='Offers'),
      path('activity',views.AddActivity, name='Offers'),
      path('vacancies',views.vacancies, name='vacancies'),
     path('activities',views.activities, name='activities'),
     path('apply',views.apply, name='apply'),
     path('pdf',views.pdf_request, name='pdf_request'),
     path('info',views.std_pdf_request, name='std_pdf_request'),
     path('eligibility_role', views.eligibility_role, name='eligibility_role'),
     path('eligibility_package', views.eligibility_package, name='eligibility_package'),
     path('eligibility_location', views.eligibility_location, name='eligibility_location'),
     path('eligibility_branch', views.eligibility_branch, name='eligibility_branch'),
     path('eligibility_form', views.eligibility_form, name='eligibility_form'),
     path('analysis',views.analysis, name='analysis'),
     path('personalise',views.personalise, name='personalise'),
     ]
