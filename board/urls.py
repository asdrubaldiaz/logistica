from django.conf.urls import url
from django.views.i18n import javascript_catalog
from . import views

js_info_dict = {
    'packages': ('board',),
}

urlpatterns = [
    url(r'^$', views.entregas_list, name='entregas_list'),
	url(r'^entrega/(?P<pk>\d+)/$', views.entrega_detail, name='entrega_detail'),
	url(r'^entrega/new/$', views.entrega_new, name='entrega_new'),
	url(r'^entrega/(?P<pk>\d+)/edit/$', views.entrega_edit, name='entrega_edit'),
	url(r'^entrega/(?P<pk>\d+)/remove/$', views.entrega_remove, name='entrega_remove'),
	url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
	url(r'^entrega/(?P<pk>\d+)/comment/$', views.add_comment_to_entrega, name='add_comment_to_entrega'),
	url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
]