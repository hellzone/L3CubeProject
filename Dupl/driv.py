import os
import time
import os.path

direc=raw_input("Enter the directory")                  
os.chdir(direc)                                       
os.system("find . -type f > drive")                   #Command for listing files 
#f=open("drive","a")
#f.close()
f=open("drive","r")
arr=f.readlines()
for i in range(0,len(arr)-1):
    arr[i]=arr[i][:len(arr[i])-1]+""             #replace "\n" by ""
f.close()

#print arr
output=list()

for line in arr:
    #line=line[:len(line)-1]+""
    #print line
    k=line.split("/")                            #Extracting only file name 
    output.append(k[len(k)-1])

for i in range (0,len(output)-1):                   
    for j in range (0,len(output)-1):                 
        if output[j]>output[j+1]:
            output[j],output[j+1]=output[j+1],output[j]
            arr[j],arr[j+1]=arr[j+1],arr[j]


count=len(output)
i=0
while i<(count-1):      
    if output[i]==output[i+1]:
        r=os.system("md5sum "+ arr[i])           #checking md5sum for duplication
        rr=os.system("md5sum "+ arr[i+1])
        
        if str(r).split()[0]==str(rr).split()[0]:
            print "Duplicate"
            ch=raw_input("Delete yes of no??")
            if ch=='yes':                                  
                if time.ctime(os.path.getctime(arr[i]))>time.ctime(os.path.getctime(arr[i+1])):     #Remove latest file if dupliacte present
                    os.remove(arr[i])
                    arr.remove(arr[i])
                    output.remove(output[i])
                    i-=1
                    count-=1
                else:
                    
                    os.remove(arr[i+1])
                    arr.remove(arr[i+1])
                    output.remove(output[i+1])
                    i-=1
                    count-=1
    i+=1
#print output
