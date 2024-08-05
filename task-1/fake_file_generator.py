from pathlib import Path
from faker import Faker
from random import randint

#Зробив шоб згенерувати рандомні файли
fake = Faker()

fake_dir = Path(fake.word())
fake_dir.mkdir(parents=True, exist_ok=True)

MAX_DIR_IN = 5
MAX_FILES_IN = 10

for _ in range(randint(1, MAX_DIR_IN)):
    fake_dir_in = fake_dir/fake.word()
    fake_dir_in.mkdir(parents=True, exist_ok=True)
    
for el in fake_dir.iterdir():
    for _ in range(randint(1, MAX_FILES_IN)):
        fake_file = el/fake.file_name()
        with open(fake_file, "w"):
            pass
        
print("Done")
        