import re

class Util:
    '''Esta clase aporta expresionres regulares de validación y mensajes de
    error adecuados'''
    RE_NO_EMPTY = re.compile(r'^(?=.*\S).+$', flags=re.DOTALL)
    '''Valida la existencia de algún carácter distinto de espacio en blanco'''
    RE_STR = re.compile(r'^.*$', flags=re.DOTALL)
    '''Valida cualquier cadena de caracteres'''
    RE_ANY_WORD_CHAR = re.compile(r'^(?=.*\w).+$', flags=re.DOTALL)
    '''Valida la existencia de al menos un carácter de palabra'''
    RE_USERNAME = re.compile(r'^(?=\w\w)(?![\d_][\d_])[\w.-]{4,16}$')
    '''Valida un nombre de usuario de entre 4 y 16 caracteres y que comienze por
     al menos dos letras. Solo puede contener números, letras, guiones
    bajos, medios y puntos'''
    ERR_USERNAME = 'Usuario no válido: El usuario tendrá entre 4 y 16 caracteres, comenzará por dos letras y solo puede contener números, letras, guiones bajos, guiones medios y puntos'
    '''Mensaje de error para un usuario no válido'''    
    RE_PASSWORD = re.compile(
        r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[\w.-]{4,32}$')
    '''Valida una contraseña de entre 4 y 32 caracteres y que contenga un
     dígito, una minúscula y una mayúscula. Solo puede contener números,
     letras, guiones bajos, medios y puntos'''
    ERR_PASSWORD = '''Contraseña no válida: La contraseña tendrá entre 4 y 32
        caracteres y contendrá al menos, un dígito, una minúscula y una
        mayúscula; además solo puede contener números, letras, guiones
        bajos, medios y puntos'''
    '''Mensaje de error para una contraseña no válida'''     
    RE_EMAIL = re.compile(
        r'^[_a-z]([.-]?[0-9a-z]+)*@[_a-z]([.-]?[0-9a-z]+)*\.[a-z]{2,8}$',
        re.IGNORECASE)
    '''Valida un e-mail'''    
    ERR_EMAIL = 'El e-mail no es válido o tiene una longitud excesiva'
    '''Mensaje de error para un e-mail no válido'''
    RE_FILENAME = re.compile(
    r'^[._-]?(?=\w)(?!_)[\w.-]*(?=\w)(?!_)\w$', re.IGNORECASE)
    '''Valida un nombre de fichero:
    *   Puede comenzar por: ., _, -
    *   El siguiente carácter: una letra o un número
    *   Le seguiran 0 o más caracteres: letra, numero, ., _, -
    *   Terminará con: una letra o un número'''    
    RE_ANY_EXT = re.compile(r'^.+(?:\.[0-9a-z]+)?$')
    '''Valida cualquier extensión incluso vacía en el nombre de fichero'''
    RE_IMG_EXT = re.compile(r'^.+\.(?:png|jpg|jpeg|bmp|gif)$')
    '''Valida la extendión de un fichero de imagen'''
    ERR_FILENAME = '''El nombre del fichero no reune los requisitos.
        Puede comenzar por '.', '_' o '-', el siguiente carácter será una
        letra o un número, le seguiran 0 o más caracteres de tipo
        letra, numero, '.', '_' o '-', y terminará con: una letra o un número'''
    '''Mensaje de error para un nombre de fichero muy largo'''
    ERR_FILENAME_EXT = 'La extensión de fichero subida no es válida'    
    '''Mensaje de error para una extensión de fichero no válida'''
    RE_URL_SECTION = re.compile(r'^[\w@-]+$')
    '''Valida una sección de URL compuesta únicamente de letras
    números, guiones bajos o medios'''
    ERR_URL_SECTION = '''Una sección de URL puede estar compuesta únicamente
    de letras números, guiones bajos o medios. Ejemplo:
    bienvenid@s-usuari@s_y_amig@s'''
    '''Mensaje de error para una sección de URL inválida'''

    # Tipos de mensaje que puede haber
    MSG_NONE = 0
    '''Ningún mensaje'''
    MSG_SUCCESS = 1
    '''Hay mensajes de éxito'''
    MSG_ERROR = 2
    '''Hay mensajes de error'''
