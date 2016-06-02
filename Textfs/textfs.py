import sys
def create(filename,content):										#create new internal file
	l = len(content)											#calculate size of internal file
	size = 0
	for i in range(l) :
		size = int(size) + len(content[i])
	
	f=open("textfscontroller",'r')
	file_content=f.read()
	f.seek(0)
	lines=f.readlines()
	f.close()
	m=file_content.find("$1$ "+filename)
	if m == -1 :
		if file_content == "" or int(lines[1].split()[3]) == 0 :		#add super block, metadata and file content in empty filesystem
			f=open("textfscontroller",'w')
			f.write("Total Files : 1\nTotal Size : "+str(size)+"\n#1#\n1"+"\t"+filename + "\t"+str(size) +" Bytes"+ "\n$1$ " + filename + "\n")
			for i in content :
				f.write(i)
			f.write("\n\n")
			f.close()
		else :												#add super block, metadata and file content in existing filesystem
			files = int(lines[0].split()[3])+1
			tsize = int(lines[1].split()[3])+int(size)
			i=3
			while lines[i].split()[0] == str(i-2) :
				i+=1
			f=open("textfscontroller",'w')
			rt=file_content.index("#1#")
			m=file_content[rt+3:].index(lines[i].split()[0])			#add super block and metadata in already existing filesystem
			f.write("Total Files : "+str(files)+"\nTotal Size : "+str(tsize)+file_content[rt-1:m-1+rt+3] + "\n" + str(i-2) + "\t"+str(filename)+"\t"+str(size) +" Bytes"+ "\n"+file_content[m+rt+3:])
			f.close()
			
			f=open("textfscontroller",'a')						#add file content
			f.write("$1$ "+filename+ "\n")
			for i in content :									
				f.write(i)
			f.write("\n\n")
			f.close()
		print "File created successfully!!!"
	else :
		print "File already exists"

def delete(filename):											#delete internal file
	'''
	To delete a file:
	Delete metadata, and content
	Also decrement the value of total number of files and total size of filesystem
	'''
	f=open("textfscontroller",'r')
	file_content=f.read()
	f.close()
	m=file_content.find("$1$ "+filename)
	if m != -1 :
		f=open("textfscontroller",'w')							#delete entry from meta data
		m=file_content.index(filename)
		g=file_content[m+len(str(filename)):].index("\n")
		f.write(file_content[:m-3] +file_content[m+len(str(filename))+g:])
		f.close()
		
		f=open("textfscontroller",'r')							#delete file content
		file_content=f.read()
		f.close()
		m=file_content.index("$1$ "+filename)			
		n=file_content[m+len(str(filename)):].find("$1$")
		f=open("textfscontroller",'w')
		if n != -1 :
			f.write(file_content[:m-1] + "\n" + file_content[m+len(str(filename))+n:])
		else :
			f.write(file_content[:m-1] + "\n")
		f.close()
		
		f=open("textfscontroller",'r')							#delete details of file from super block
		lines=f.readlines()
		f.seek(0)
		file_content=f.read()
		f.close()
		m=file_content.index("#1#")
		i=3
		tsize = 0
		if file_content[m+3:] != "\n" :
			while lines[i].split()[0] != "$1$" :
				tsize = tsize + int(lines[i].split()[2])
				i=i+1
		f=open("textfscontroller",'w')
		f.write("Total Files : "+str(i-3)+"\nTotal Size : "+str(tsize)+file_content[m-1:])
		f.close()
		print "File Deleted!!!"
	else :
		print "File not found!!!"
	
def echo(filename):												#display contents of file
	f=open("textfscontroller",'r')
	file_content=f.read()
	m=file_content.find("$1$ "+filename)
	if m != -1 :
		n=file_content[m+len(str(filename)):].find(filename)
		x = file_content[m+(2*len(str(filename)))+n:]
		y = x.find("$1$")
		if y != -1 :
			print x[:y]
		else :
			print x
	else :
		print "File Not Found!!!"

def list():													#list the files in file system
	f = open("textfscontroller","r")
	lines=f.readlines()
	i=3
	f.seek(0)
	file_content=f.read()
	m=file_content.find("$1$")
	if m != -1 :
		while lines[i].split()[0]!="$1$":
			print lines[i]
			i+=1
	else :
		print "Empty FileSystem"
		
def help():													#display usage of commands
	print "1) create 'filename':\tcreate an internal file 'filename'\n2) delete 'filename':\t delete internal file 'filename'\n3) echo 'filename':\tdisplay contents of internal file 'filename'\n4) copy 'internal_file' 'external_file':\tcopy content of 'external_file' to 'internal_file'\n5) list:\tlist all files in file system\n6)reset:\treset/format the file system\n"
	
def reset():													#format filesystem
	f=open("textfscontroller",'w')
	f.write("Total Files : 0\nTotal Size : 0\n#1#")
	f.close()
	print "file system formatted\a"

f=open("textfscontroller",'a')
f.close()
while True:
	cmd = raw_input()
	command=cmd.split()
	if command[0]=="create":
		content=sys.stdin.readlines()
		create(command[1],content)
		
	elif command[0]=="delete":
		delete(command[1])
	
	elif command[0] == "copy" :									#copy external file into file system
		f = open(command[2],"r")
		fc = f.read()
		f.close()
		create(command[1],fc)
	
	elif command[0] == "list" :			
		list()
	
	elif command[0] == "echo" :
		echo(command[1])
		
	elif command[0] == "help" :
		help()
		
	elif command[0] == "reset":			
		reset()
		
	else:
		print "type 'help' for more options"
