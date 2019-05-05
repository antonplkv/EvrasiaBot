from config import shelve_name
import shelve
from utils import set_user
i = 0
with shelve.open(shelve_name) as storage:
    for id in storage.keys():
        set_user(id)
        print(id, end=" ")
        i+=1
    print(i)