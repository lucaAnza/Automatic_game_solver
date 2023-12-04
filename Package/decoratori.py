import functools
import datetime
from colorama import Fore, Style
import print_coloured as p


def timestamp_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        exe_time = (end_time - start_time)
        p.print_cyan_ts(f"Tempo esecuzione {func.__name__}: {exe_time}")
        return result  # restituisce il risultato della chiamata originale
    return wrapper
