from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path('about/',views.about, name="about"),
    path("contact/",views.contact,name="contact"),
    path('service/',views.service,name="service"),
    path('ukcolleges/',views.ukcollege,name="ukcollege"),
    path('cancolleges/',views.cancollege,name="cancollege"),
    path('uscolleges/',views.uscollege,name="uscollege"),
    path('auscolleges/',views.auscollege,name="auscollege"),
    path('colleges/harvard/', views.us_harvard_unversity_detail_view, name='us_harvard_university_detail'),
    path('colleges/stanford/', views.us_stanford_unversity_detail_view, name='us_stanford_unversity_detail'),
    path('colleges/mit/', views.us_mit_unversity_detail_view, name='us_mit_university_detail'),
    path('colleges/yale/', views.us_yale_unversity_detail_view, name='us_yale_unversity_detail'),
    path('colleges/pinceton/', views.us_princeton_unversity_detail_view, name='us_princeton_unversity_detail'),
    path('colleges/uchicago/', views.us_uchicago_detail_view, name='us_uchicago_detail'),
    path('colleges/colombia/', views.us_colombia_university_detail_view, name='us_colombia_university_detail'),
    path('colleges/upenncylvenea/', views.us_upenncylvenea_detail_view, name='us_upenncylvenea_detail'),
    path('colleges/cit/', views.us_cit_detail_view, name='us_cit_detail'),
    path('colleges/duke/', views.us_duke_university_detail_view, name='us_duke_university_detail'),
    
    
    
# Uk colleges

   path('colleges/uoxford/', views.uk_uoxford_detail_view, name='uk_uoxford_detail'),
   path('colleges/cambridge/', views.uk_cambridge_university_detail_view, name='uk_cambridge_university_detail'),
   path('colleges/ic/', views.uk_ic_london_detail_view, name='uk_ic_london_detail'),
   path('colleges/ucl/', views.uk_ucl_detail_view, name='uk_ucl_detail'),
   path('colleges/edienburgh/', views.uk_university_of_edienburgh_detail_view, name='uk_university_of_edienburgh_detail'),
   path('colleges/manchester/', views.uk_umanchester_detail_view, name='uk_umanchester_detail'),
   path('colleges/kcl/', views.uk_kcl_details_view, name='uk_kcl_details'),
   path('colleges/lsc/', views.uk_lsc_details_view, name='uk_lsc_details'),
   path('colleges/bristol/', views.uk_university_of_bristol_detail_view, name='uk_university_of_bristol_detail'),
   path('colleges/warwick/', views.uk_university_of_warwick_detail_view, name='uk_university_of_warwick_detail'),
   
   
   
   
#Aus Colleges   
   path('colleges/melboure/',views.aus_university_of_melbourne_detail_view,name="aus_university_of_melbourne_detail"),
   path('colleges/sydney/',views.aus_university_of_sydney_detail_view,name="aus_university_of_sydney_detail"),
   path('colleges/anu/',views.aus_anu_detail_view,name="aus_anu_detail"),
   path('colleges/queensland/',views.aus_university_of_queensland_detail_view,name="aus_university_of_queensland_detail"),
   path('colleges/monas/',views.aus_monash_university_detail_view,name="aus_monash_university_detail"),
   path('colleges/unsw/',views.aus_unsw_detail_view,name="aus_unsw_detail"),
   path('colleges/uwa/',views.aus_uwa_detail_view,name="aus_uwa_detail"),
   path('colleges/uoadelaide/',views.aus_uoadelaide_detail_view,name="aus_uoadelaide_detail"),
   path('colleges/uts/',views.aus_uts_detail_view,name="aus_uts_detail"),
   path('colleges/mu/',views.aus_mu_detail_view,name="aus_mu_detail"),
  
  #cancolleges
  
  path('colleges/uot/',views.can_uot_detail_view,name="can_uot_detail"),
  path('colleges/ubc/',views.can_ubc_detail_view,name="can_ubc_detail"),
  path('colleges/muu/',views.can_muu_detail_view,name="can_muu_detail"),
  path('colleges/alberta/',views.can_uo_alberta_detail_view,name="can_uo_alberta_detail"),
  path('colleges/waterloo/',views.can_uo_waterloo_detail_view,name="can_uo_waterloo_detail"),
  path('colleges/qu/',views.can_qu_detail_view,name="can_qu_detail"),
  path('colleges/qu/',views.can_wu_detail_view,name="can_wu_detail"),
  path('colleges/sfu/',views.can_sfu_detail_view,name="can_sfu_detail"),
  path('colleges/uoo/',views.can_uoo_detail_view,name="can_uoo_detail"),
  path('colleges/du/',views.can_du_detail_view,name="can_du_detail"),
  
  
  
]