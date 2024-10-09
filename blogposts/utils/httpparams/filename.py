from re import Pattern
from .util import Util
from .param import Param

class Filename(Param):
    '''Esta clase aporta métodos de validación para nombres de fichero'''    
    
    def __init__(self) -> None:
        super().__init__()
    
    def validate(self, filename: str, re_ext: Pattern = Util.RE_ANY_EXT,
        max_length = 128, ignore_empty = True,
        field_title = '') -> str:
        '''
        Valida el nombre de un fichero. Si no pasa la validación
        se agregará el mensaje a los errores.
        Parameters:
            filename (str): Nombre del fichero a validar.
            re_ext (Pattern): Patrón de validación de la extensión.
            ignore_empty (bool): Ignorar nombre de fichero vacío.
        Returns:
            str: El nombre del fichero pasado.
        '''
        if not filename and ignore_empty:
            return filename
        
        msg_header = f'"{field_title}": ' if field_title else ''
        if not Util.RE_FILENAME.fullmatch(filename):
            self.add_error(f'{msg_header}{Util.ERR_FILENAME}')

        if not re_ext.fullmatch(filename):
            self.add_error(Util.ERR_FILENAME_EXT)

        if len(filename) > max_length:            
            self.add_error(f'{msg_header
            }Longitud del nombre de fichero excedida, tamaño: {
            len(filename)}, máximo: {max_length}, ')            
        
        return filename
    
