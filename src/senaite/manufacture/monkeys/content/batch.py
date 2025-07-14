from senaite.manufacture import check_installed

@check_installed(None)
def getBatchSize(self):  # noqa camelcase, but compliant with AT's
    """Returns the batch size
    """
    return self.getField("BatchSize").get(self)

@check_installed(None)
def getReleasedQuantity(self):  # noqa camelcase, but compliant with AT's
    """Returns the batch released quantity
    """
    return self.getField("ReleasedQuantity").get(self)