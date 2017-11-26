from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^followup/', views.case_list, name='follow_list'),
	url(r'^case/(?P<pk>\d+)/$', views.case_detail, name='case_detail'),
	url(r'^case/new/$', views.case_new, name='case_new'),

]