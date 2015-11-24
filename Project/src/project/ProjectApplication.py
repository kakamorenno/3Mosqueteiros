
from pyglass.app.PyGlassApplication import PyGlassApplication

#___________________________________________________________________________________________________ LegoManApplication
class ProjectApplication(PyGlassApplication):

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: debugRootResourcePath
    @property
    def debugRootResourcePath(self):
        return ['..', '..', 'resources']

#___________________________________________________________________________________________________ GS: splashScreenUrl
    @property
    def splashScreenUrl(self):
        return 'splashscreen.png'

#___________________________________________________________________________________________________ GS: appID
    @property
    def appID(self):
        return 'Project'

#___________________________________________________________________________________________________ GS: appGroupID
    @property
    def appGroupID(self):
        return 'Project'

#___________________________________________________________________________________________________ GS: mainWindowClass
    @property
    def mainWindowClass(self):
        from project.ProjectMainWindow import ProjectMainWindow
        return ProjectMainWindow

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    ProjectApplication().run()
