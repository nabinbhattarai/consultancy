from django.urls import path
from . import views
from django_distill import distill_path

# Generator functions must return iterable of argument tuples (or None)
def get_none():
    return None

urlpatterns=[
    distill_path("",views.home, name="home", distill_func=get_none, distill_file="index.html"),
    distill_path('about/',views.about, name="about", distill_func=get_none),
    distill_path("contact/",views.contact,name="contact", distill_func=get_none),
    distill_path('service/',views.service,name="service", distill_func=get_none),
    distill_path('ukcolleges/',views.ukcollege,name="ukcollege", distill_func=get_none),
    distill_path('cancolleges/',views.cancollege,name="cancollege", distill_func=get_none),
    distill_path('uscolleges/',views.uscollege,name="uscollege", distill_func=get_none),
    distill_path('auscolleges/',views.auscollege,name="auscollege", distill_func=get_none),
    distill_path('colleges/harvard/', views.us_harvard_unversity_detail_view, name='us_harvard_university_detail', distill_func=get_none),
    distill_path('colleges/stanford/', views.us_stanford_unversity_detail_view, name='us_stanford_unversity_detail', distill_func=get_none),
    distill_path('colleges/mit/', views.us_mit_unversity_detail_view, name='us_mit_university_detail', distill_func=get_none),
    distill_path('colleges/yale/', views.us_yale_unversity_detail_view, name='us_yale_unversity_detail', distill_func=get_none),
    distill_path('colleges/pinceton/', views.us_princeton_unversity_detail_view, name='us_princeton_unversity_detail', distill_func=get_none),
    distill_path('colleges/uchicago/', views.us_uchicago_detail_view, name='us_uchicago_detail', distill_func=get_none),
    distill_path('colleges/colombia/', views.us_colombia_university_detail_view, name='us_colombia_university_detail', distill_func=get_none),
    distill_path('colleges/upenncylvenea/', views.us_upenncylvenea_detail_view, name='us_upenncylvenea_detail', distill_func=get_none),
    distill_path('colleges/cit/', views.us_cit_detail_view, name='us_cit_detail', distill_func=get_none),
    distill_path('colleges/duke/', views.us_duke_university_detail_view, name='us_duke_university_detail', distill_func=get_none),
    
    
    
# Uk colleges

   distill_path('colleges/uoxford/', views.uk_uoxford_detail_view, name='uk_uoxford_detail', distill_func=get_none),
   distill_path('colleges/cambridge/', views.uk_cambridge_university_detail_view, name='uk_cambridge_university_detail', distill_func=get_none),
   distill_path('colleges/ic/', views.uk_ic_london_detail_view, name='uk_ic_london_detail', distill_func=get_none),
   distill_path('colleges/ucl/', views.uk_ucl_detail_view, name='uk_ucl_detail', distill_func=get_none),
   distill_path('colleges/edienburgh/', views.uk_university_of_edienburgh_detail_view, name='uk_university_of_edienburgh_detail', distill_func=get_none),
   distill_path('colleges/manchester/', views.uk_umanchester_detail_view, name='uk_umanchester_detail', distill_func=get_none),
   distill_path('colleges/kcl/', views.uk_kcl_details_view, name='uk_kcl_details', distill_func=get_none),
   distill_path('colleges/lsc/', views.uk_lsc_details_view, name='uk_lsc_details', distill_func=get_none),
   distill_path('colleges/bristol/', views.uk_university_of_bristol_detail_view, name='uk_university_of_bristol_detail', distill_func=get_none),
   distill_path('colleges/warwick/', views.uk_university_of_warwick_detail_view, name='uk_university_of_warwick_detail', distill_func=get_none),
   
   
   
   
#Aus Colleges   
   distill_path('colleges/melboure/',views.aus_university_of_melbourne_detail_view,name="aus_university_of_melbourne_detail", distill_func=get_none),
   distill_path('colleges/sydney/',views.aus_university_of_sydney_detail_view,name="aus_university_of_sydney_detail", distill_func=get_none),
   distill_path('colleges/anu/',views.aus_anu_detail_view,name="aus_anu_detail", distill_func=get_none),
   distill_path('colleges/queensland/',views.aus_university_of_queensland_detail_view,name="aus_university_of_queensland_detail", distill_func=get_none),
   distill_path('colleges/monas/',views.aus_monash_university_detail_view,name="aus_monash_university_detail", distill_func=get_none),
   distill_path('colleges/unsw/',views.aus_unsw_detail_view,name="aus_unsw_detail", distill_func=get_none),
   distill_path('colleges/uwa/',views.aus_uwa_detail_view,name="aus_uwa_detail", distill_func=get_none),
   distill_path('colleges/uoadelaide/',views.aus_uoadelaide_detail_view,name="aus_uoadelaide_detail", distill_func=get_none),
   distill_path('colleges/uts/',views.aus_uts_detail_view,name="aus_uts_detail", distill_func=get_none),
   distill_path('colleges/mu/',views.aus_mu_detail_view,name="aus_mu_detail", distill_func=get_none),
  
  #cancolleges
  
  distill_path('colleges/uot/',views.can_uot_detail_view,name="can_uot_detail", distill_func=get_none),
  distill_path('colleges/ubc/',views.can_ubc_detail_view,name="can_ubc_detail", distill_func=get_none),
  distill_path('colleges/muu/',views.can_muu_detail_view,name="can_muu_detail", distill_func=get_none),
  distill_path('colleges/alberta/',views.can_uo_alberta_detail_view,name="can_uo_alberta_detail", distill_func=get_none),
  distill_path('colleges/waterloo/',views.can_uo_waterloo_detail_view,name="can_uo_waterloo_detail", distill_func=get_none),
  distill_path('colleges/qu/',views.can_qu_detail_view,name="can_qu_detail", distill_func=get_none),
  distill_path('colleges/qu/',views.can_wu_detail_view,name="can_wu_detail", distill_func=get_none),
  distill_path('colleges/sfu/',views.can_sfu_detail_view,name="can_sfu_detail", distill_func=get_none),
  distill_path('colleges/uoo/',views.can_uoo_detail_view,name="can_uoo_detail", distill_func=get_none),
  distill_path('colleges/du/',views.can_du_detail_view,name="can_du_detail", distill_func=get_none),
]