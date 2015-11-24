from nimble import *
from pyglass.widgets.PyGlassWidget import PyGlassWidget


#___________________________________________________________________________________________________ Assignment1Widget
class SadnessWidget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment1Widget."""
        super(SadnessWidget, self).__init__(parent, **kwargs)
        self.sadnessBtn.clicked.connect(self._handleSadness)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleSadness(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        cmds.select("smile_frown_control", replace=True)
        cmds.setAttr("blendShape1.head_frown", 1)
        cmds.setAttr("blendShape1.head_smile", 0)
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
