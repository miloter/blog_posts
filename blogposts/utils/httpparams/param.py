from re import Pattern
from .util import Util

class Param:        
    '''Esta clase aporta métodos de validación y us sistema de
    gestión de éxitos y errores'''    
    
    def __init__(self) -> None:
        self.__typeMsgs = Util.MSG_NONE
        self.__msgs = []
    
    def add_error(self, message: str) -> None:
        '''
        Agrega un nuevo error a la lista.
        Parameters:
            message (str): Mensaje de error.        
        '''
        self.__msgs.append({ 'message': message, 'category': 'error' })
        self.__typeMsgs = Util.MSG_ERROR
    
    def add_success(self, message: str) -> None:
        '''
        Agrega un nuevo mensaje de éxito a la lista.
        Parameters:
            message (str): Mensaje de éxito.
        '''
        self.__msgs.append({ 'message': message, 'category': 'success' })
        self.__typeMsgs = Util.MSG_SUCCESS

    def validate(self, value: str, re: Pattern,
        msg_error: str, max_length = 4096, ignore_empty = False,
        field_title = '') -> str:        
        '''
        Valida contenido en formato de cadena. Si no pasa la validación
        se agregará el mensaje a los errores.
        Parameters:
            value (str): Valor a validar.
            re (Pattern): Expresión regular de validación.
            msg_error (str): Mensaje de error en caso de que no se pase la validación.
            max_length (int): Lóngitud máxima del valor a validar.
            ignore_empty (bool): Indica si se ignoran los argumentos vacíos.
            field_title (str): Nombre del campo opcional.
        Returns:
            str: El Valor a validar.
        '''
        if not value and ignore_empty:
            return value
        
        msg_header = f'"{field_title}": ' if field_title else ''
        if not re.fullmatch(value):
            self.add_error(f'{msg_header}{msg_error}')            
        
        if len(value) > max_length:            
            self.add_error(f'{msg_header}Longitud excedida, tamaño: {
                len(value)}, máximo: {max_length}, ')
        
        return value
        
    def is_error(self):
        '''Devuelve un valor que indica si se han producido errores'''
        return self.__typeMsgs == Util.MSG_ERROR
    
    def is_success(self):
        '''Devuelve un valor que indica si se han producido éxitos'''
        return self.__typeMsgs == Util.MSG_SUCCESS
    
    def is_none(self):
        '''Devuelve un valor que indica si se no se han
        producido éxitos ni errores'''
        return self.__typeMsgs == Util.MSG_NONE
    
    def get_msgs(self) -> list[dict]:
        '''
        Devuelve la lista de mensajes.
        Returns:
            list[dict] Una lista de diccionarios conteniendo la lista de
            mensajes, donde cada mensaje es de la forma:
            { 'message': '...', 'category': 'success' | 'error' }
        '''        
        return self.__msgs

