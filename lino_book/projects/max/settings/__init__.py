# -*- coding: UTF-8 -*-
# Copyright 2012-2016 Luc Saffre
# License: BSD (see file COPYING for details)

"""A special settings module to be used as DJANGO_SETTINGS_MODULE when
Sphinx generates the Lino docs.

It contains (almost) all modlib modules, which makes no sense in
practice and would maybe raise errors if you try to initialize a
database or validate the models, but it is enough to have autodocs do
its job.  And that's all we want.

"""

from lino.projects.std.settings import *

import lino_xl


class Site(Site):

    demo_fixtures = 'std few_countries demo demo2'.split()

    verbose_name = "Lino Max"
    version = lino_xl.__version__

    project_name = 'lino_xl_max'

    project_model = 'contacts.Person'

    # languages = 'en de fr'
    languages = 'en de fr et nl pt-br es'

    # user_types_module = 'lino.modlib.users.roles'
    user_types_module = 'lino_xl.lib.xl.roles'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()

        yield 'lino.modlib.system'
        # yield 'lino.modlib.gfks'
        yield 'lino.modlib.users'
        yield 'lino.modlib.changes'
        yield 'lino.modlib.languages'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.properties'
        yield 'lino_xl.lib.contacts'
        yield 'lino.modlib.plausibility'
        yield 'lino_xl.lib.addresses'
        yield 'lino_xl.lib.humanlinks'  # requires Person to be Born
        yield 'lino_xl.lib.polls'

        yield 'lino.modlib.uploads'
        yield 'lino_xl.lib.notes'
        yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.cal'
        yield 'lino_xl.lib.extensible'
        yield 'lino_xl.lib.reception'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_xl.lib.cv'
        yield 'lino_xl.lib.boards'
        yield 'lino_xl.lib.topics'
        yield 'lino_xl.lib.postings'
        yield 'lino_xl.lib.households'

        yield 'lino_xl.lib.concepts'
        yield 'lino_xl.lib.pages'
        yield 'lino_xl.lib.beid'
        yield 'lino.modlib.wkhtmltopdf'
        yield 'lino_xl.lib.appypod'

        yield 'lino.modlib.tinymce'
        yield 'lino.modlib.export_excel'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(country_code='BE')

    def do_site_startup(self):
        # lino_xl.lib.reception requires some workflow to be imported
        from lino_xl.lib.cal.workflows import feedback
        super(Site, self).do_site_startup()

