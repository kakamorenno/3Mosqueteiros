
from pyglass.compile.PyGlassApplicationCompiler import PyGlassApplicationCompiler
from pyglass.compile.SiteLibraryEnum import SiteLibraryEnum

from project.ProjectApplication import ProjectApplication

#___________________________________________________________________________________________________ LegoManCompiler
class ProjectCompiler(PyGlassApplicationCompiler):
    """A class for..."""

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: siteLibraries
    @property
    def siteLibraries(self):
        return [SiteLibraryEnum.PYSIDE]

#___________________________________________________________________________________________________ GS: binPath
    @property
    def binPath(self):
        return ['..', '..', 'bin']

#___________________________________________________________________________________________________ GS: appFilename
    @property
    def appFilename(self):
        return 'Project'

#___________________________________________________________________________________________________ GS: appDisplayName
    @property
    def appDisplayName(self):
        return 'Project'

#___________________________________________________________________________________________________ GS: applicationClass
    @property
    def applicationClass(self):
        return ProjectApplication

#___________________________________________________________________________________________________ GS: iconPath
    @property
    def iconPath(self):
        return ['apps', 'Project']

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    ProjectCompiler().run()

