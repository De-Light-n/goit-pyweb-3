
import sys
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

folders = []

def get_folders(sourse: Path):
    if sourse.is_dir():
        for el in sourse.iterdir():
            if el.is_dir():
                folders.append(el)
                get_folders(el)
                
def copy_files(dirrectory: Path, destination: Path):
    for el in dirrectory.iterdir():
        if el.is_file():
            exten = el.suffix[1:]
            dest = destination / exten
            try:
                dest.mkdir(exist_ok=True, parents=True)
                copyfile(el, dest / el.name)
            except OSError as err:
                logging.info(err)
                
if __name__=="__main__":
    """ Перший аргумет: sourse
        Другий аргумент: destination(по замовчуванню dist)
    """
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    lenth = len(sys.argv)
    if lenth < 2:
        logging.info("Недостатньо елементів")
        exit()
    elif lenth < 3:
        sourse = Path(sys.argv[1])
        destination = Path("dist")
    else:
        sourse = Path(sys.argv[1])
        destination = Path(sys.argv[2])
    
    get_folders(sourse)
    threads = []
    for folder in folders:
        th = Thread(target=copy_files, args=(folder, destination))
        th.start()
        threads.append(th)
        
    [th.join() for th in threads]
    
    logging.info("Сортування завершено")
    
    
    