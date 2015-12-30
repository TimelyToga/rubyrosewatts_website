from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import rubyrosewatts_app.settings

urlpatterns = patterns('',
    url(r'^$', 'rubyrosewatts_app.views.home'),
    url(r'^about$', 'rubyrosewatts_app.views.about'),

    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': rubyrosewatts_app.settings.CSS_DIR}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': rubyrosewatts_app.settings.IMG_DIR}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': rubyrosewatts_app.settings.JS_DIR}),
    (r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': rubyrosewatts_app.settings.FONT_DIR}),
)
