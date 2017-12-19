from ftw.keywordwidget.field import ChoicePlus
from ftw.keywordwidget.widget import KeywordFieldWidget
from ftw.tagging import _
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from z3c.form.interfaces import IAddForm, IEditForm
from zope import schema
from zope.interface import alsoProvides


class ITagging(model.Schema):

    model.fieldset(
        'tags',
        label=_(u'label_schema_tags', default=u'Tags'),
        fields=[
            'tags',
        ],
    )

    directives.widget('tags', KeywordFieldWidget)
    tags = schema.List(
        title=_(u'label_tags', default=u'Tags'),
        value_type=ChoicePlus(
            title=u'Multiple',
            vocabulary='tags',
        ),
        required=False,
        missing_value=(),
    )

    # Show field only on edit/add forms.
    directives.omitted('tags', )
    directives.no_omit(IEditForm, 'tags', )
    directives.no_omit(IAddForm, 'tags', )


alsoProvides(ITagging, IFormFieldProvider)
