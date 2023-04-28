import Register
import time
# Start to run
def initial(args):
    #load all the params from ini.config
    print("success~")

while(True):
    usersList=Register.Register.readUsers();
    Register.Register.processRegister(usersList)
    time.sleep(1)
    usersList=[]
    if usersList==[]:
        print('no more users stop')
        break