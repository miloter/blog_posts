'''Implementa métodos para buscar similitudes con caracteres,  palabras, y
frases y conversión a formas padre'''

class SimilWords:
    '''Implementa métodos para buscar similitudes con caracteres,  palabras, y
    frases y conversión a formas padre'''
    
    def __init__(self, to_lower: bool = False) -> None:
        '''        
        Parameters:
            to_lower (bool): Si es True el alfabeto padre estará en minúsculas
            y si es False en mayúsculas.        
        '''
        self.__to_lower = to_lower
        # La búsqueda insensible a mayúsculas y minúsculas y los acentos
        # se implementa en un diccionario
        self.__alpha = {}
        # Devuelve una búsqueda inversa, es decir, a partir del
        # código padre, devuelve el carácter padre
        self.__parent = {}

        self.__alpha['F'] = 70
        self.__alpha['f'] = 70
        self.__alpha['G'] = 71
        self.__alpha['g'] = 71
        self.__alpha['H'] = 72
        self.__alpha['h'] = 72
        self.__alpha['J'] = 74
        self.__alpha['j'] = 74
        self.__alpha['K'] = 75
        self.__alpha['k'] = 75
        self.__alpha['L'] = 76
        self.__alpha['l'] = 76
        self.__alpha['M'] = 77
        self.__alpha['m'] = 77
        self.__alpha['Q'] = 81
        self.__alpha['q'] = 81
        self.__alpha['R'] = 82
        self.__alpha['r'] = 82
        self.__alpha['T'] = 84
        self.__alpha['t'] = 84
        self.__alpha['V'] = 86
        self.__alpha['v'] = 86
        self.__alpha['W'] = 87
        self.__alpha['w'] = 87
        self.__alpha['X'] = 88
        self.__alpha['x'] = 88
        self.__alpha['A'] = 65
        self.__alpha['a'] = 65
        self.__alpha['Á'] = 65
        self.__alpha['á'] = 65
        self.__alpha['À'] = 65
        self.__alpha['à'] = 65
        self.__alpha['Â'] = 65
        self.__alpha['â'] = 65
        self.__alpha['Ã'] = 65
        self.__alpha['ã'] = 65
        self.__alpha['Ä'] = 65
        self.__alpha['ä'] = 65
        self.__alpha['Å'] = 65
        self.__alpha['å'] = 65
        self.__alpha['Æ'] = 65
        self.__alpha['æ'] = 65
        self.__alpha['E'] = 69
        self.__alpha['e'] = 69
        self.__alpha['É'] = 69
        self.__alpha['é'] = 69
        self.__alpha['È'] = 69
        self.__alpha['è'] = 69
        self.__alpha['Ê'] = 69
        self.__alpha['ê'] = 69
        self.__alpha['Ë'] = 69
        self.__alpha['ë'] = 69
        self.__alpha['I'] = 73
        self.__alpha['i'] = 73
        self.__alpha['Í'] = 73
        self.__alpha['í'] = 73
        self.__alpha['Ì'] = 73
        self.__alpha['ì'] = 73
        self.__alpha['Î'] = 73
        self.__alpha['î'] = 73
        self.__alpha['Ï'] = 73
        self.__alpha['ï'] = 73
        self.__alpha['O'] = 79
        self.__alpha['o'] = 79
        self.__alpha['Ó'] = 79
        self.__alpha['ó'] = 79
        self.__alpha['Ò'] = 79
        self.__alpha['ò'] = 79
        self.__alpha['Ô'] = 79
        self.__alpha['ô'] = 79
        self.__alpha['Õ'] = 79
        self.__alpha['õ'] = 79
        self.__alpha['Ö'] = 79
        self.__alpha['ö'] = 79
        self.__alpha['Ø'] = 79
        self.__alpha['ø'] = 79
        self.__alpha['Œ'] = 79
        self.__alpha['œ'] = 79
        self.__alpha['U'] = 85
        self.__alpha['u'] = 85
        self.__alpha['Ú'] = 85
        self.__alpha['ú'] = 85
        self.__alpha['Ù'] = 85
        self.__alpha['ù'] = 85
        self.__alpha['Ü'] = 85
        self.__alpha['ü'] = 85
        self.__alpha['Û'] = 85
        self.__alpha['û'] = 85
        self.__alpha['C'] = 67
        self.__alpha['c'] = 67
        self.__alpha['Ç'] = 67
        self.__alpha['ç'] = 67
        self.__alpha['N'] = 78
        self.__alpha['n'] = 78
        self.__alpha['Ñ'] = 78
        self.__alpha['ñ'] = 78
        self.__alpha['S'] = 83
        self.__alpha['s'] = 83
        self.__alpha['Š'] = 83
        self.__alpha['š'] = 83
        self.__alpha['Z'] = 90
        self.__alpha['z'] = 90
        self.__alpha['Ž'] = 90
        self.__alpha['ž'] = 90
        self.__alpha['Y'] = 89
        self.__alpha['y'] = 89
        self.__alpha['Ÿ'] = 89
        self.__alpha['ÿ'] = 89
        self.__alpha['Ý'] = 89
        self.__alpha['ý'] = 89
        self.__alpha['D'] = 68
        self.__alpha['d'] = 68
        self.__alpha['Ð'] = 68
        self.__alpha['ð'] = 68
        self.__alpha['P'] = 80
        self.__alpha['p'] = 80
        self.__alpha['Þ'] = 80
        self.__alpha['þ'] = 80
        self.__alpha['B'] = 66
        self.__alpha['b'] = 66
        self.__alpha['ß'] = 66

        # Estable el alfabeto de los caracteres padre.
        self.__parent[70] = 'f' if self.__to_lower else 'F'
        self.__parent[71] = 'g' if self.__to_lower else 'G'
        self.__parent[72] = 'h' if self.__to_lower else 'H'
        self.__parent[74] = 'j' if self.__to_lower else 'J'
        self.__parent[75] = 'k' if self.__to_lower else 'K'
        self.__parent[76] = 'l' if self.__to_lower else 'L'
        self.__parent[77] = 'm' if self.__to_lower else 'M'
        self.__parent[81] = 'q' if self.__to_lower else 'Q'
        self.__parent[82] = 'r' if self.__to_lower else 'R'
        self.__parent[84] = 't' if self.__to_lower else 'T'
        self.__parent[86] = 'v' if self.__to_lower else 'V'
        self.__parent[87] = 'w' if self.__to_lower else 'W'
        self.__parent[88] = 'x' if self.__to_lower else 'X'
        self.__parent[65] = 'a' if self.__to_lower else 'A'
        self.__parent[69] = 'e' if self.__to_lower else 'E'
        self.__parent[73] = 'i' if self.__to_lower else 'I'
        self.__parent[79] = 'o' if self.__to_lower else 'O'
        self.__parent[85] = 'u' if self.__to_lower else 'U'
        self.__parent[67] = 'c' if self.__to_lower else 'C'
        self.__parent[78] = 'n' if self.__to_lower else 'N'
        self.__parent[83] = 's' if self.__to_lower else 'S'
        self.__parent[90] = 'z' if self.__to_lower else 'Z'
        self.__parent[89] = 'y' if self.__to_lower else 'Y'
        self.__parent[68] = 'd' if self.__to_lower else 'D'
        self.__parent[80] = 'p' if self.__to_lower else 'P'
        self.__parent[66] = 'b' if self.__to_lower else 'B'

    def __ipos(self, c: str) -> int:
        '''Devuelve la posición de una letra en un criterio relativo de
        comparación que ignora diferencias entre mayúsculas y minúsculas
        y sus signos'''
        p = self.__alpha.get(c)
        return p if p is not None else c    

    def parent_char(self, c: str) -> str:
        '''Devuelve el carácter padre del carácter pasado como argumento. Si no
        tiene padre devuelve el mismo carácter'''     
        c2 = self.__parent.get(self.__ipos(c))
        return c2 if c2 is not None else c
    
    def parent_string(self, s: str) -> str:
        '''Devuelve la cadena en formato padre de la cadena pasada como
        argumento'''
        return ''.join(self.parent_char(c) for c in s)
    
    def icmp(self, s1: str, s2: str) -> int:
        '''
        Compara dos cadenas sin tener en cuenta la diferencia entre
        mayúsculas y minúsculas ni los signos. Devuelve 0 si son iguales.
        -1 si la primera es menor que la segunda. 1 si la primera es mayor
        que la segunda.
        Parameters:
            s1 (str): Primera cadena que se comparará.
            s2 (str): Segunda cadena que se comparará.
        Returns:
            int
        '''
        limit = len(s1) if len(s1) <= len(s2) else len(s2)        
        for i in range(limit):
            # Buscamos la posición de la letra de la primera cadena
            j = self.__ipos(s1[i])
            # Buscamos la posición de la letra de la segunda cadena
            k = self.__ipos(s2[i])
            if j > k:
                return 1
            elif j < k:
                return -1                    
            
        if len(s1) == len(s2):
            return 0
        elif len(s1) > len(s2):
            return 1
        else:
            return -1
    def similitud(self, s: str, t: str) -> float:
        '''
        Devuelve el porcentaje de similitud entre dos cadenas en una escala
        de 0 a 100. El algoritmo es una implementacón del algoritmo de la
        distancia de Levenshtein. El algoritmo de comparación no tiene en
        cuenta la diferencia entre mayúsculas y minúsculas e ignora los
        signos, como los acentos, tildes, etc.
        Parameters:
            s (str): Primera cadena a comparar con la segunda.
            t (str): Segunda cadena a comparar con la primera.
        Returns:
            float: El porcentaje de similitud en una escala de 0 a 100.
        '''     
        costo = 0
        m = len(s)
        n = len(t)

        # Verifica que exista algo que comparar
        if m == 0 and n == 0:
            return 100
        elif m == 0 or n == 0:
            return 0        

        # Generamos espacio de almacenamiento
        d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]        
        
        # Llena la primera columna y la primera fila.
        for i in range(m + 1):
            d[i][0] = i
        for j in range(n + 1):
            d[0][j] = j
        
        # Recorre la matriz llenando cada unos de los pesos.
        # i columnas, j renglones
        for i  in range(1, m + 1):
            # Recorre para j
            for j in range(1, n + 1):
                # Si son iguales en posiciones equidistantes el peso es 0
                # de lo contrario el peso suma a uno
                costo = (
                    0 if self.__ipos(s[i - 1]) == self.__ipos(t[j - 1])
                    else 1
                )
                d[i][j] = min(min(d[i - 1][j] + 1,  # Eliminacion
                    d[i][j - 1] + 1),               # Inserccion 
                    d[i - 1][j - 1] + costo)        # Sustitucion                    

        # Calculamos el porcentaje de cambios en la palabra.
        if len(s) > len(t):
            return 100 * (1 - d[m][n] / len(s))
        else:
            return 100 * (1 - d[m][n] / len(t))

    def get_words(self, s: str, is_parent: bool = True) -> list[str]:
        '''
        Devuelve una lista con las palabras de una cadena.
        Parameters:
            s (str): Cadena de la que se extraerán las palabras.
            is_parent (bool): Indica si se devuelven en formato padre o no.
        Returns:
            list[str]: La lista con las palabras.
        '''
        start = 0
        length = 0
        list = []
        if is_parent:
            s = self.parent_string(s)

        for i in range(len(s)):
            if s[i].isalnum():
                if length == 0:
                    start = i                
                length += 1
            elif length > 0:
                list.append(s[start:start + length])
                length = 0                    

        if length > 0:
            list.append(s[start:start + length])        

        return list
      
    def normalize(self, s: str, is_parent: bool = True, delimiter: str = ' ') -> str:
        '''
        Devuelve una cadena normalizada.
        Parameters:
            s (str): Cadena que se normalizará.
            is_parent (bool): Si es verdadero devuelve las palabras en formato
            cadena padre.
            delimiter (str): Delimitador de las palabras, usualmente el espacio
            en blanco ' '.
        Returns:
            str: Cadena normalizada.
        '''
        return delimiter.join(self.get_words(s, is_parent))
    
    def simil_text(self, s1: str, s2: str, subset: bool = True,
        penalize_num_words: bool = False) -> float:
        '''
        Compara dos textos y devuelve un porcentaje de similitud. La
        comparación es insensible a mayúsculas, minúsculas y letras con signo.
        Parameters:
            s1 (str): Primera cadena que se comparará.
            s2 (str): Segunda cadena que se comparará.
            subset (bool): Si es verdadero la similitud se hace en relación
            a la cadena.
            penalize_num_words (bool): Si es verdadero se aplica la
            penalización cuando el número de palabras en ambos textos es
            diferente.
        Returns:
            float: Un porcentaje de similitud de 0 a 100.     
        '''
        APROX_PERCENT = 50
        REDUCTOR = 0.89
        ws1 = self.get_words(s1, False)
        ws2 = self.get_words(s2, False)

        if len(ws1) == 0 and len(ws2) == 0:
            return 100
        elif len(ws1) == 0 or len(ws2) == 0:
            return 0        

        if len(ws1) > len(ws2):
            aux = ws1
            ws1 = ws2
            ws2 = aux        

        total = 0
        count = 0
        # Buscamos inicialmente coincidencias del 100%
        for i in range(len(ws1)):
            for j in range(len(ws2)):
                if ws2[j]:
                    if self.icmp(ws1[i], ws2[j]) == 0:
                        total += 100 * (REDUCTOR if (i != j and not subset)
                            else 1)
                        count += 1
                        ws1[i] = ''
                        ws2[j] = ''
                        break                                                        

        while count < len(ws1):
            max = 0
            imax = jmax = -1
            for i in range(len(ws1)):
                if ws1[i]:
                    for j in range(len(ws2)):
                        if ws2[j]:
                            p = self.similitud(ws1[i], ws2[j])
                            # Se penaliza si la coincidencia es menor de 50
                            if p < APROX_PERCENT:
                                p *= REDUCTOR                            

                            # Se aplica el coeficiente reductor si están en distinta
                            # posición y no se busca coincidencia de subconjunto
                            if i != j and not subset:
                                p *= REDUCTOR                            

                            if p > max:
                                max = p
                                imax = i
                                jmax = j

                                # Si coincide totalmente, no se sigue comprobando
                                if max == 100:
                                    break                                                                                                        

                    # Si coincide totalmente, no se sigue comprobando
                    if max == 100:
                        break                                                

            if max > 0:
                total += max
                ws1[imax] = ''
                ws2[jmax] = ''
                count += 1
            else:
                break            

        # Si se compara como subconjunto, entonces se usa la cadena más corta
        p = total / (len(ws1) if subset else len(ws2))

        if penalize_num_words:
            # Corregimos con un factor basado en la diferencia de palabras
            p *= 0.99 ** abs(len(ws1) - len(ws2))
        
        return p
    
