from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.http import HttpResponseRedirect
from .models import *
from django.db.models import Q


def index(request):
    return render(request, 'blog/index.html')

class SectionPageView(TemplateView):

    template_name = 'blog/sections.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = SectionModel.objects.all()
        return context

class ThemePageView(TemplateView):

    template_name = 'blog/theme.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['themes'] = ThemeModel.objects.filter(section=kwargs.get('pk'))
        return context
    
    
class PablicationsView(TemplateView):

    template_name = 'blog/pablications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pablics'] = PablicationModel.objects.filter(theme=kwargs.get('pk'))
        return context


class DescriptionsView(TemplateView):

    template_name = 'blog/description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descriptions'] = DescriptionModel.objects.filter(pablic=kwargs.get('pk'))
        return context



"""class SearchForSiteView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        search_all_contents = TableOfContents.objects.filter(Q(nameDescription__icontains=search_query) |
                                                             Q(descriptionTheme__icontains=search_query))
        
        if search_all_contents:
            v = search_all_contents.values()[0]['themeDescription_id']
            link_contents = TableOfContents.objects.filter(themeDescription=v)
            short_description = link_contents.filter().values()[0]['descriptionTheme'][:50] + '...'
            context = {'link_contents': link_contents, 'short_description': short_description}
        else:
            return HttpResponseRedirect('/')
        return render(request, 'diary/search.html', context)"""
            
        
