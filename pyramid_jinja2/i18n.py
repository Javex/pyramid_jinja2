from pyramid import i18n
from pyramid.threadlocal import get_current_request


class GetTextWrapper(object):

    def __init__(self, domain):
        self.domain = domain

    @property
    def localizer(self):
        return i18n.get_localizer(get_current_request())

    def gettext(self, message):
        return self.localizer.translate(message,
                                        domain=self.domain)

    def ngettext(self, singular, plural, n):
        return self.localizer.pluralize(singular, plural, n,
                                        domain=self.domain)
