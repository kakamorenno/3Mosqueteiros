# Assignment2Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ Assignment2Widget
class Assignment2Widget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Assignment2Widget."""
        super(Assignment2Widget, self).__init__(parent, **kwargs)

        self.homeBtn.clicked.connect(self._handleReturnHome)
        #self.homeBtn.clicked.connect(self._makeCyl)
        self.smileSlider.setRange(0,100)
        self.smileSlider.valueChanged.connect(self._handleSmileSlider)
        self.frownSlider.setRange(0,100)
        self.frownSlider.valueChanged.connect(self._handleFrownSlider)
        self.eyes.setRange(-100,100)
        self.eyes.valueChanged.connect(self._handleEyeHeight)
#===================================================================================================
#                                                                                 H A N D L E R S
    def _makeCyl(self):
        r = 50
        a = 2.0*r
        y = (0, 1, 0)
        c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
        cmds.select(c)
        response = nimble.createRemoteResponse(globals())
        response.put('name', c)

    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')

    def _handleSmileSlider(self,value_s):
        #print(value)
        response=nimble.createRemoteResponse(globals())
        #response.put('name', cmds.setAttr('polyCylinder1.radius', value))
        scaledVal_s = float(value_s)/100
        response.put('name', cmds.setAttr('blendShape1.pasted__face', scaledVal_s))

    def _handleFrownSlider(self, value_f):
        response=nimble.createRemoteResponse(globals())
        scaledVal_f = float(value_f)/100
        response.put('name', cmds.setAttr('blendShape1.pasted__face1', scaledVal_f))

    def _handleEyeHeight(self, value_e):
        response=nimble.createRemoteResponse(globals())
        scaledVal_e = float(value_e)/100
        translateEyeball = (scaledVal_e)*(0.13)+5.941
        response.put('name', cmds.setAttr('blendShape7.pasted__pasted__face2', scaledVal_e))
        #print(translateEyeball)
        response.put('name', cmds.setAttr('pasted__pasted__L_eye1.translateY', translateEyeball))
        response.put('name', cmds.setAttr('pasted__pasted__R_eye1.translateY', translateEyeball))
