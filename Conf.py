from configparser import ConfigParser, ExtendedInterpolation

configfile = 'config.ini'

__configs = ConfigParser(interpolation=ExtendedInterpolation())
__configs.read(configfile)


def get(section, prop):
    if section in __configs:
        if prop in __configs[section]:
            return __configs[section][prop]
        else:
            print('Configurator. Property: {prop} does not exist')
    else:
        print('Configurator. Section: {section} does not exist')
