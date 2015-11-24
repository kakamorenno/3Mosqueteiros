from PySide import QtGui

from pyglass.windows.PyGlassWindow import PyGlassWindow

from project.views.home.ProjectHomeWidget import ProjectHomeWidget
from project.views.sadness.SadnessWidget import SadnessWidget


#___________________________________________________________________________________________________ MayaPyMainWindow
class ProjectMainWindow(PyGlassWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, **kwargs):
        PyGlassWindow.__init__(
            self,
            widgets={
                'home':ProjectHomeWidget,
                'sadness':SadnessWidget,
            title='Project' ,
        **kwargs )

        self.setMinimumSize(1024,480)
        self.setContentsMargins(0, 0, 0, 0)

        widget = self._createCentralWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)

        self.setActiveWidget('home')
