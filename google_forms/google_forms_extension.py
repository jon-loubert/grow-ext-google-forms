#from babel import Locale
#for key, territory in Locale('es').territories.iteritems():
#    print territory
#
from jinja2.ext import Extension


class GoogleFormsExtension(Extension):

    def __init__(self, environment):
        super(GoogleFormsExtension, self).__init__(environment)
        environment.filters['']
