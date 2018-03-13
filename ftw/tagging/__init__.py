from zope.i18nmessageid import MessageFactory

taggingMessageFactory = MessageFactory('ftw.tagging')

_ = taggingMessageFactory


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
