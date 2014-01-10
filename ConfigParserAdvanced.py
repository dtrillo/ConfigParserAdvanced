""" ConfigParserAdvanced,
developer by David Trillo Montero
write me at manejandodatos@gmail.com

Visit my website: http://www.manejandodatos.es """
# Versión 0.7.0 - 20140110

import ConfigParser

class ConfigParserAdvanced():
    def __init__(self, sfile, main_section = None, getdefault = ''):
        self.file = sfile
        self.reload()
        self.main_section = main_section
        self.getdefault = getdefault

    def reload(self):
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(self.file)

    def defaultValue(self, value):
        self.getdefault = value

    def read(self, sfilename):
        return self.config.read(sfilename)

    def sections(self):
        """ Sections of the Config File """
        return self.config.sections()

    def main_section(self, new_section):
        """ Change Section """
        self.main_section = new_section

    def options(self, new_section):
        """ Options from a NEW SECTION, that become Main_Section """
        self.main_section = new_section
        return self.config.options(self.main_section)

    def add_section(self, new_section):
        """ Add a New section """
        self.main_section = new_section
        self.config.add_section(self.main_section)

    # GET functions
    def get(self, section, option, defval = None):
        """ Get a VALUE of an option, of the SECTION"""
        self.main_section = section
        try:
            return self.config.get(self.main_section, option)
        except:
            if defval != None:
                return defval
            else:
                return self.getdefault
    def getboolean(self, section, option):
        """ GET a BOOLEAN Value of an OPTION of the SECTION """
        self.main_section = section
        try:
            return self.config.getboolean(self.main_section, option)
        except:
            return False
    def getfloat(self, section, option):
        """ GET a BOOLEAN Value of an OPTION of the SECTION """
        self.main_section = section
        try:
            return self.config.getfloat(self.main_section, option)
        except:
            return False
    def getint(self, section, option):
        """ GET a BOOLEAN Value of an OPTION of the SECTION """
        self.main_section = section
        try:
            return self.config.getint(self.main_section, option)
        except:
            return False
    def has_option(self, section,option):
        """ Exists OPTION in SECTION """
        self.main_section = section
        try:
            return self.config.has_option(self.main_section, option)
        except:
            return False


    # get FROM the Main_SECTION
    def options2(self):
        """ Options from Main_Section """
        return self.options(self.main_section)
    def get2(self, option):
        """ Get a VALUE of an option, of the MAIN_SECTION"""
        return self.get(self, self.main_section, option)
    def getboolean2(self, option):
        """ GET a BOOLEAN Value of an OPTION of the SECTION """
        return self.getboolean(self.main_section, option)
    def getint2(self, option):
        """ GET a BOOLEAN Value of an OPTION of the SECTION """
        return self.getint(self.main_section, option)
    def getfloat2(self, option):
        """ GET a BOOLEAN Value of an OPTION of the SECTION """
        return self.getfloat(self.main_section, option)
    def has_option2(self, option):
        """ Exists OPTION in MAIN_SECTION """
        return self.has_option(self.main_section, option)
    def has_section(self, section):
        try:
            return self.config.has_section(section)
        except:
            return False

    # Write Data to self.File
    def writedata(self):
        sf = open(self.file,"w") # Necesito el fichero INI "preparado" para grabar información
        self.config.write(sf)
        sf.close()
    def set(self, section, option, value = None, bSave = True):
        if self.config.has_section(section) == False:
            self.config.add_section(section)
        self.main_section = section
        self.config.set(self.main_section, option, value)
        if bSave:
            self.writedata()

    # Write OPTION-VALUE to MAIN_SECTION
    def set2(self, option, value = None, bSave = True):
        """ Set data on the MAIN_SECTION  """
        self.set(self.main_section, option, value, bSave)
