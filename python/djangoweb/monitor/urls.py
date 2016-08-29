from django.conf.urls import patterns, url
from monitor import views
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<question_id>\d+)/$',
                           views.detail, name='detail'),
                       url(r'^(?P<question_id>\d+)/results/$',
                           views.results, name='results'),
                       url(r'^(?P<question_id>\d+)/vote/$',
                           views.vote, name='vote'),
                       url(r'^form', views.form, name='form'),
                       url(r'^home', views.home, name='home'),  # new
                       )
