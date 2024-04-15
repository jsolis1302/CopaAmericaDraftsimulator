from django.urls import  re_path, path
from CupDraft import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # re_path(r'^country/$',views.countryApi),
    path('country/',views.countryApi),
    path('startDraft/',views.startDraft),
    path('group/<str:groupName>',views.groupApi),
    path('kophase/',views.setKOPhase),
    re_path(r'^groupA/$',views.groupAApi),
    re_path(r'^groupB/$',views.groupBApi),
    re_path(r'^groupC/$',views.groupCApi),
    re_path(r'^groupD/$',views.groupDApi),
    path('resetDraft/',views.ResetApp),
    path("country/<str:countryCode>",views.getCountryByCode)

] 
