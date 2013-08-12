from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  RedirectView.as_view(url = reverse_lazy('auth_login')), {'url': ''}, name='index'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.auth_urls')),
    url(r'', include('social_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}, name='logout'),
    url(r'^accounts/profile/', RedirectView.as_view(url = reverse_lazy('auth_login')), {'url': ''}),

)
