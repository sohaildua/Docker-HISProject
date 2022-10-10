from git import Repo
import getpass
import os

full_local_path = os.getcwd()
full_local_path_new=''

try:
    full_local_path_new=os.mkdir(full_local_path+ '\project')
    print(full_local_path_new)
except OSError:
    print ("Creation of the directory %s failed" % full_local_path_new)
else:
    print ("Successfully created the directory %s " % full_local_path_new)
username = input("enter your github username")
password = input("enter your github password")
remote = f"http://sdgamer007:Sdgamer%40005@github.com/sdgamer007/PythonScripts.git"

Repo.clone_from(remote, full_local_path_new)
