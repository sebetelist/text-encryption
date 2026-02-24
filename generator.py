from pathlib import Path
from itertools import count

def get_unique_file(base_name, extension):
    counter = count(1, 1)
    while True:
        num = next(counter)
        file_path = Path(f"{base_name}_{num}{extension}")
        
        if not file_path.exists():
            return file_path
    
  






