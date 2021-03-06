"""Views for Zinnia quick entry"""
try:
    from urllib.parse import urlencode
except:  # Python 2
    from urllib import urlencode

from django import forms
from django.shortcuts import redirect
from django.utils.html import linebreaks
from django.views.generic.base import View
from django.utils.encoding import smart_str
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.template.defaultfilters import slugify
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.utils import timezone

from zinnia.models.entry import Entry
from zinnia.managers import DRAFT
from zinnia.managers import PUBLISHED
from zinnia.settings import MARKUP_LANGUAGE


class QuickEntryForm(forms.ModelForm):
    """
    Form for posting an entry quickly.
    """

    class Meta:
        model = Entry
        exclude = ('comment_count',
                   'pingback_count',
                   'trackback_count')


class QuickEntry(View):
    """
    View handling the quick post of a short Entry.
    """

    def get(self, request, *args, **kwargs):
        """
        GET only do a redirection to the index
        """
        return redirect('/')

    def post(self, request, *args, **kwargs):
        """
        Handle the datas for posting a quick entry,
        and redirect to the admin in case of error or
        to the entry's page in case of success.
        """
        idyoutube = request.POST.get('idyoutube')
        if idyoutube:
            html_text = "<iframe width='100%' height='300px' class='embed-responsive-item' src='//www.youtube.com/embed/" + idyoutube + "' frameborder='0' allowfullscreen></iframe>"
        else:
            html_text = ""
            
        data = {
            'title': request.POST.get('titleyoutube'),
            'slug': slugify(request.POST.get('titleyoutube')),
            'status': DRAFT,
            'sites': [Site.objects.get_current().pk],
            'authors': [1],
            'content_template': 'zinnia/_entry_detail.html',
            'detail_template': 'entry_detail.html',
            'creation_date': timezone.now(),
            'last_update': timezone.now(),
            'content': html_text,
            }
        form = QuickEntryForm(data)
        if form.is_valid():
            form.instance.content = self.htmlize(form.cleaned_data['content'])
            entry = form.save()
            return redirect(entry)

        data = {'title': smart_str(request.POST.get('titleyoutube', '')),
                'content': smart_str(self.htmlize(html_text)),
                'slug': slugify(request.POST.get('title', '')),
                'authors': request.user.pk,
                'sites': Site.objects.get_current().pk}
        return redirect('/')
        # return redirect('%s?%s' % (reverse('admin:zinnia_entry_add'),
        #                            urlencode(data)))

    def htmlize(self, content):
        """
        Convert to HTML the content if the MARKUP_LANGUAGE
        is set to HTML to optimize the rendering and avoid
        ugly effect in WYMEditor.
        """
        if MARKUP_LANGUAGE == 'html':
            return linebreaks(content)
        return content