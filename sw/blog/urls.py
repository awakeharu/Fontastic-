from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),


	url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^(?P<post_pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
	url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)edit/$', views.comment_edit, name='comment_edit'),
	url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)delete/$', views.comment_delete, name='comment_delete'),


	url(r'^post_new/$', views.post_new , name='post_new'),

	url(r'^request_new/$',views.request_new, name='request_new'),
	url(r'^(?P<pk>\d+)/request/$', views.request_detail, name='request_detail'),

	url(r'^question_new/$',views.question_new, name='question_new'),
	url(r'^(?P<pk>\d+)/question/$',views.question_detail, name='question_detail'),

	url(r'^upload_new/$',views.upload_new, name='upload_new'),
	url(r'^(?P<pk>\d+)/upload/$',views.upload_detail, name='upload_detail'),


]