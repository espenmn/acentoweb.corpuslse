# -*- coding: utf-8 -*-

# from acentoweb.corpuslse import _
#from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView
from zope.interface import Interface
#from z3c.form import interfaces

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ICorpusView(Interface):
    """ Marker Interface for ICorpusView"""


class CorpusView(DefaultView):
    #pass
    # template = ViewPageTemplateFile('corpus_view.pt')

    def __init__(self, context, request):
        super(CorpusView, self).__init__(context, request)

    def updateWidgets(self):
        super(CorpusView, self).updateWidgets()
        #self.widgets['espen'].mode = 'hidden'


    def updateFields(self):
        super(CorpusView, self).updateFields()


    def update(self):
        super(CorpusView, self).update()
