from Products.PloneTestCase import ptc
from collective.testcaselayer import common
from collective.testcaselayer import ptc as tcl_ptc


class Layer(tcl_ptc.BasePTCLayer):
    """Install ftw.tagging """

    def afterSetUp(self):
        ptc.installPackage('ftw.tagging')
        self.addProfile('ftw.tagging:default')

layer = Layer([common.common_layer])
