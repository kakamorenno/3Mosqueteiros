
from PySide import QtGui

from pyglass.widgets.PyGlassWidget import PyGlassWidget

from project.enum.UserConfigEnum import UserConfigEnum
from project.views.home.NimbleStatusElement import NimbleStatusElement

#___________________________________________________________________________________________________ LegoManHomeWidget
class ProjectHomeWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of LegoManHomeWidget."""
        super(ProjectHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True

        self.sadnessBtn.clicked.connect(self._handleSadness)

        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()

        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True) )
        statusLayout.addWidget(self._nimbleStatus)
#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _activateWidgetDisplayImpl
    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleRaiseArm
    def _handleSadness(self):
        self.mainWindow.setActiveWidget('sadness')

