from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import TemplateView

from home.views import HomeView
from contact.views import ContactCreate, ContactSuccessView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact/add/$', ContactCreate.as_view()),
    url(r'^contact_success/$', ContactSuccessView.as_view())
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
