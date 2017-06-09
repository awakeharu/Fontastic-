from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', views.index, name='index'),

	#post board
	url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post_new/$', views.post_new , name='post_new'),
	
	url(r'^(?P<post_pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
	url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)edit/$', views.comment_edit, name='comment_edit'),
	url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)delete/$', views.comment_delete, name='comment_delete'),

	# call board
	url(r'^call_new/$',views.call_new, name='call_new'),
	url(r'^(?P<pk>\d+)/call/$',views.call_detail, name='call_detail'),
	url(r'^(?P<call_pk>\d+)/call_comment/new/$', views.call_comment_new, name='call_comment_new'),
	url(r'^(?P<call_pk>\d+)/call_comment/(?P<pk>\d+)edit/$', views.call_comment_edit, name='call_comment_edit'),
	url(r'^(?P<call_pk>\d+)/call__comment/(?P<pk>\d+)delete/$', views.call_comment_delete, name='call_comment_delete'),

	#question board
	url(r'^question_new/$',views.question_new, name='question_new'),
	url(r'^(?P<pk>\d+)/question/$',views.question_detail, name='question_detail'),
	url(r'^(?P<question_pk>\d+)/question_comment/new/$', views.question_comment_new, name='question_comment_new'),
	url(r'^(?P<question_pk>\d+)/question_comment/(?P<pk>\d+)edit/$', views.question_comment_edit, name='question_comment_edit'),
	url(r'^(?P<question_pk>\d+)/question_comment/(?P<pk>\d+)delete/$', views.question_comment_delete, name='question_comment_delete'),

	#upload
	url(r'^upload_new/$',views.upload_new, name='upload_new'),
	url(r'^(?P<pk>\d+)/upload/$',views.upload_detail, name='upload_detail'),

]
