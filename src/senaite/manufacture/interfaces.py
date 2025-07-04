# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from bika.lims.interfaces import IDoNotSupportSnapshots
from senaite.core.interfaces import IHideActionsMenu
from senaite.lims.interfaces import ISenaiteLIMS
from zope.interface import Interface
#from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ISenaiteManufactureLayer(ISenaiteLIMS):
    """Marker interface that defines a browser layer."""


class IContentFolder(IHideActionsMenu, IDoNotSupportSnapshots):
    """Marker interface for basic containers
    """


class IProducts(IContentFolder):
    """Marker interface for container of Diseases
    """


class IProduct(Interface):
    """Marker interface for Disease objects
    """
