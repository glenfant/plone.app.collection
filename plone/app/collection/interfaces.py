from zope.interface import Interface
from plone.registry import field

class ICollection(Interface):
    """ """
    pass

class ICollectionRegistryReader(Interface):
    """Marker interface for the registry adapter"""

class IQueryOperation(Interface):
    title = field.TextLine(title=u"Title")
    description = field.Text(title=u"Description")
    operation = field.TextLine(title=u"Operation")
    widget = field.TextLine(title=u"Widget")

class IQueryField(Interface):
    title = field.TextLine(title=u"Title")
    description = field.Text(title=u"Description")
    enabled = field.Bool(title=u"Enabled")
    sortable = field.Bool(title=u"Sortable")
    operations = field.List(title=u"Operations", value_type=field.DottedName(title=u"Operation ID"))
    vocabulary = field.TextLine(title=u"Vocabulary")
    group = field.TextLine(title=u"Group")
