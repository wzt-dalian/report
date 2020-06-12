import os

rootdir='C:\\Users\\wzt_d\Desktop\\Ning'

def listAllFiles(rootPath,mlist):
    list=os.listdir(rootPath)
    for i in range(0,len(list)):
        path=os.path.join(rootPath,list[i])
        if os.path.isfile(path):
            mlist.append(path)
        elif os.path.isdir(path):
            listAllFiles(path,mlist)

if(__name__ == "__main__"):
       mylist=[]
       listAllFiles(rootdir, mylist)
       print(*[x for x in mylist], sep= "\n")
       print(len(mylist))