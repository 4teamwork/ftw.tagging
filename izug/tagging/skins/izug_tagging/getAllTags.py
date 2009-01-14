## Script (Python) "getAllTags"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
from Products.Archetypes import atapi
from Products.CMFCore.utils import getToolByName

catalog = getToolByName(context, "portal_catalog")
items = atapi.DisplayList(())

for tag in catalog.uniqueValuesFor("tags"):
    items.add(tag,tag)

return items
