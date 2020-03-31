from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


app_name = 'blog'

urlpatterns= [
    path('', index, name='index'),
    path('sections/', SectionPageView.as_view(), name='sections'),
    path('themes/<int:pk>/', ThemePageView.as_view(), name='themes'),
    path('pablic/<int:pk>/', PablicationsView.as_view(), name='pablic'),
    path('description/<int:pk>/', DescriptionsView.as_view(), name='description'),
  #  path('search/', SearchForSiteView.as_view(), name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
