import atexit
from pathlib import Path
from time import time


path = Path('date')
DATE = float(path.read_text()) if path.exists() else time()


@atexit.register
def writer():
    path.write_text(str(DATE))
