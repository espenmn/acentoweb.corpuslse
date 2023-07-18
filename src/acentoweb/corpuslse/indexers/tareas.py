# -*- coding: utf-8 -*-

from plone.app.contenttypes.interfaces import IDocument
from plone.dexterity.interfaces import IDexterityContent
from plone.dexterity.interfaces import IDexterityContainer
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """ Dummy to prevent indexing other objects thru acquisition """
    raise AttributeError('This field should not indexed here!')


@indexer(IDexterityContainer)  # ADJUST THIS to custom content type!
def tareasIndexer(obj):
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

    for indeksfield in indeksfields:
        if hasattr(obj, indeksfield):
            if getattr(obj, indeksfield) != None:  #Maybe check for length ?
                #indeks.add(getattr(obj, indekfield))
                indeks.add(indeksfield)

    #import pdb; pdb.set_trace()
    obj.tareas = indeks
    return indeks
