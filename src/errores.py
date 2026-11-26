class ErrorLenguaje(Exception):
    """Base de todos los errores del lenguaje."""

class ErrorLexico(ErrorLenguaje):
    pass

class ErrorSintactico(ErrorLenguaje):
    pass

class ErrorEjecucion(ErrorLenguaje):
    pass
