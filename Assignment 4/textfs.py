import sys
def create(filename,content):
	f=open("textfscontroller",'r')
	file_content=f.read()
	f.close()
	f=open("textfscontroller",'r')
	lines=f.readlines()
	f.close()
	
	if file_content=="":
		f=open("textfscontroller",'a')
		f.write("1"+" "+filename + "\n$1$ " + filename + "\n")
		for i in content :
			f.write(i)
		f.write("\n\n")
		f.close()
	else :
		i=0
		while lines[i].split()[0] == str(i+1) :
			i+=1
		f=open("textfscontroller",'w')
		m=file_content.index(lines[i].split()[0])
		if m<3 :
			f.write(str(i+1) + " "+str(filename)+"\n"+file_content[m:])
		else :
			f.write(file_content[:m-1] + "\n" + str(i+1) + " "+str(filename)+"\n"+file_content[m:])
		f.close()
		f=open("textfscontroller",'a')
		f.write("$1$ "+filename+ "\n")
		for i in content :
			f.write(i)
		f.write("\n\n")
		f.close()

def delete(filename):
	f=open("textfscontroller",'r')
	file_content=f.read()
	f.close()
	f=open("textfscontroller",'w')
	m=file_content.index(filename)
	if m<3 :	
		f.write(file_content[m+len(str(filename))+1:])
	else :
		f.write(file_content[:m-3] +file_content[m+len(str(filename)):])
	f.close()
	f=open("textfscontroller",'r')
	file_content=f.read()
	f.close()
	m=file_content.index(filename)
	n=file_content[m+len(str(filename)):].find("$1$")
	f=open("textfscontroller",'w')
	if n != -1 :
		f.write(file_content[:m-4] + file_content[m+len(str(filename))+n:])
	else :
		f.write(file_content[:m-4])
	f.close()
def echo(filename):
	f=open("textfscontroller",'r')
	file_content=f.read()
	m=file_content.index(filename)
	#print m
	if m != -1 :
		n=file_content[m+len(str(filename)):].find(filename)
		#print n
		x = file_content[m+(2*len(str(filename)))+n:]
		y = x.find("$1$")
		if y != -1 :
			print x[:y]
		else :
			print x
	else :
		print "File Not Found!!!"

f=open("textfscontroller",'a')
f.close()			
while True:
	cmd = raw_input()
	command=cmd.split()
	count=0
	if command[0]=="create":
		count+=1
		content=sys.stdin.readlines()
		create(command[1],content)
		print "File created successfully!!!"
		
	if command[0]=="delete":
		delete(command[1])
		print "File Deleted!!!"
	
	if command[0] == "copy" :
		f = open(command[2],"r")
		fc = f.read()
		f.close()
		create(command[1],fc)
		print "File copied successfully!!!"
	
	if command[0] == "list" :
		f = open("textfscontroller","r")
		lines=f.readlines()
		i=0
		while lines[i].split()[0]!="$1$":
			print lines[i]
			i+=1
	
	if command[0] == "echo" :
		echo(command[1])
