from django.conf import settings

def naniano(request):
    naniano = {
        'naniano_name': settings.NANIANO_NAME,
        'naniano_footer': settings.NANIANO_MESSAGE_FOOTER,
        'naniano_link_footer': settings.NANIANO_LINK_FOOTER,
    }

    return naniano
