from django.shortcuts import render
from django.http import HttpResponse

from .testimonials import testimonials

# Create your views here.
def home(request):
    return render(request,'main/home.html', {'testimonials': testimonials})

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def service(request):
    return render(request,'main/services.html')

def ukcollege(request):
    return render(request,'main/ukcollege.html')

def uscollege(request):
    return render(request,'main/uscollege.html')

def cancollege(request):
    return render(request,'main/cancollege.html')

def auscollege(request):
    return render(request,'main/auscollege.html')

def us_harvard_unversity_detail_view(request):
    return render(request, 'us_college_detail/harvard University_description.html')

def us_stanford_unversity_detail_view(request):
    return render(request, 'us_college_detail/stanford_university_detail.html')

def us_mit_unversity_detail_view(request):
    return render(request, 'us_college_detail/MIT_university_detail.html')


def us_yale_unversity_detail_view(request):
    return render(request, 'us_college_detail/yale_university_detail.html')


def us_princeton_unversity_detail_view(request):
    return render(request, 'us_college_detail/princeton_university_detail.html')

def us_uchicago_detail_view(request):
    return render(request, 'us_college_detail/uchicago_details.html')


def us_colombia_university_detail_view(request):
    return render(request, 'us_college_detail/columbia_university_detail.html')


def us_upenncylvenea_detail_view(request):
    return render(request, 'us_college_detail/upenncylvenea_detail.html')

def us_cit_detail_view(request):
    return render(request, 'us_college_detail/cit_university_details.html')

def us_duke_university_detail_view(request):
    return render(request, 'us_college_detail/duke_university_detail.html')

# uk colleges


def uk_uoxford_detail_view(request):
    return render(request, 'uk_college_detail/uoxford_details.html')

def uk_cambridge_university_detail_view(request):
    return render(request, 'uk_college_detail/cambridge_university_details.html')


def uk_ic_london_detail_view(request):
    return render(request, 'uk_college_detail/ic_london_detail.html')

def uk_ucl_detail_view(request):
    return render(request, 'uk_college_detail/ucl_details.html')

def uk_university_of_edienburgh_detail_view(request):
    return render(request, 'uk_college_detail/university_of_edinburgh_detail.html')

def uk_umanchester_detail_view(request):
    return render(request, 'uk_college_detail/umanchester_detail.html')

def uk_kcl_details_view(request):
    return render(request, 'uk_college_detail/kcl_details.html')

def uk_lsc_details_view(request):
    return render(request, 'uk_college_detail/lse_detail.html')

def uk_university_of_bristol_detail_view(request):
    return render(request, 'uk_college_detail/university_of_bristol_detail.html')

def uk_university_of_warwick_detail_view(request):
    return render(request, 'uk_college_detail/university_of_warwick_detail.html')


#Aus Colleges 

def aus_university_of_melbourne_detail_view(request):
    return render(request, 'aus_college_detail/university_of_melbourne_detail.html')

def aus_university_of_sydney_detail_view(request):
    return render(request, 'aus_college_detail/university_of_sydney_detail.html')

def aus_anu_detail_view(request):
    return render(request, 'aus_college_detail/anu_detail.html')

def aus_university_of_queensland_detail_view(request):
    return render(request, 'aus_college_detail/university_of_queensland_detail.html')

def aus_unsw_detail_view(request):
    return render(request, 'aus_college_detail/unsw_detail.html')

def aus_monash_university_detail_view(request):
    return render(request, 'aus_college_detail/monash_university_detail.html')

def aus_uwa_detail_view(request):
    return render(request, 'aus_college_detail/uwa_detail.html')

def aus_uoadelaide_detail_view(request):
    return render(request, 'aus_college_detail/uoadelaide_detail.html')

def aus_uts_detail_view(request):
    return render(request, 'aus_college_detail/uts_detail.html')

def aus_mu_detail_view(request):
    return render(request, 'aus_college_detail/mu_detail.html')



#university of canada

def can_uot_detail_view(request):
    return render(request, 'can_college_detail/uot_detail.html')

def can_ubc_detail_view(request):
    return render(request, 'can_college_detail/ubc_detail.html') 

def can_muu_detail_view(request):
    return render(request, 'can_college_detail/muu_detail.html') 

def can_uo_alberta_detail_view(request):
    return render(request, 'can_college_detail/uo_alberta_detail.html') 

def can_uo_waterloo_detail_view(request):
    return render(request, 'can_college_detail/uo_waterloo_detail.html') 

def can_qu_detail_view(request):
    return render(request, 'can_college_detail/qu_detail.html') 

def can_wu_detail_view(request):
    return render(request, 'can_college_detail/wu_detail.html')

def can_sfu_detail_view(request):
    return render(request, 'can_college_detail/sfu_detail.html')

def can_uoo_detail_view(request):
    return render(request, 'can_college_detail/uoo_detail.html')

def can_du_detail_view(request):
    return render(request, 'can_college_detail/du_detail.html')
















