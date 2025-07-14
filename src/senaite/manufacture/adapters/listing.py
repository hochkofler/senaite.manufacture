from bika.lims import api
from bika.lims.utils import get_link
from plone.memoize.instance import memoize
from plone.memoize.view import memoize as viewcache
from senaite.app.listing.interfaces import IListingView
from senaite.app.listing.interfaces import IListingViewAdapter
from senaite.app.listing.utils import add_column
from senaite.app.listing.utils import add_review_state
from senaite.manufacture import messageFactory as _
from senaite.manufacture import check_installed
from zope.component import adapts
from zope.component import getMultiAdapter
from zope.interface import implements


# Columns to add
ADD_COLUMNS = [
    ("BatchSize", {
        "title": _("BatchSize"),
        "sortable": False,
        "after": "Title",
    }),
    ("ReleasedQuantity", {
        "title": _("ReleasedQuantity"),
        "sortable": False,
        "after": "Title",
    }),
]


class BatchesListingAdapter(object):
    """Generic adapter for batch listings
    """
    adapts(IListingView)
    implements(IListingViewAdapter)

    # Priority order of this adapter over others
    priority_order = 99999

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    @property
    @memoize
    def senaite_theme(self):
        return getMultiAdapter(
            (self.context, self.listing.request),
            name="senaite_theme")

    def icon_tag(self, name, **kwargs):
        return self.senaite_theme.icon_tag(name, **kwargs)

    @check_installed(None)
    def folder_item(self, obj, item, index):

        batch_batch_size = api.to_utf8(
            obj.getId, default="")
            #obj.getBatchSize, default="")

        batch_ReleasedQuantity = api.to_utf8(
            obj.getId, default="")
            #obj.getReleasedQuantity, default="")

        item["BatchSize"] = batch_batch_size
        item["ReleasedQuantity"] = batch_ReleasedQuantity


    @check_installed(None)
    def before_render(self):
        # Additional columns
        rv_keys = map(lambda r: r["id"], self.listing.review_states)
        for column_id, column_values in ADD_COLUMNS:
            add_column(
                listing=self.listing,
                column_id=column_id,
                column_values=column_values,
                after=column_values.get("after", None),
                review_states=rv_keys)