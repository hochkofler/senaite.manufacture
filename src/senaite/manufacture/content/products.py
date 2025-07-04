# ===========================
# content/products.py
# ===========================

from plone.dexterity.content import Container
from plone.supermodel import model
from senaite.manufacture.interfaces import IProducts
from zope.interface import implementer


class IProductsSchema(model.Schema):
    """Schema interface
    """


@implementer(IProducts, IProductsSchema)
class Products(Container):
    """Folder for Products contents
    """