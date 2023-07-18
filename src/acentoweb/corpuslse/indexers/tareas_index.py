# -*- coding: utf-8 -*-

from plone.app.contenttypes.interfaces import IDocument
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """ Dummy to prevent indexing other objects thru acquisition """
    raise AttributeError('This field should not indexed here!')


@indexer(IDocument)  # ADJUST THIS!
def tareas_index(obj):
    """Calculate and return the value for the indexer"""
    indeks = set()
    indeksfields = [
        'pres_codigo',
        'edu_codigo',
        'infan_codigo',
        'tya_codigo',
        'rana_codigo',
        'nico_codigo',
        'simon_codigo',
        'nev_codigo',
        'chyc_codigo',
        'syp_codigo',
        'tyj_codigo',
        'teo_codigo',
        'drama_codigo',
        'pera_codigo',
        'banco_codigo',
        'asoc_codigo',
        'diacr_codigo'
    ]

    #def __init__(self, context, catalog):
    #...         self.context = context
    #...         self.catalog = catalog
    #...
    #...     def __call__(self):
    #...         return len(self.context.text)

    for indexfield in indeksfields:
        if getattr(obj, indexfield):
            indeks.add(getattr(obj, indexfield))

    obj.tareas = indeks
    return indeks
