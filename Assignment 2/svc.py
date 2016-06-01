import os.path
from time import strftime
def print_latest_version(filename):
	if os.path.isfile(filename) :
		f = open(filename,"r")
		file_contents = f.read()
		print (file_contents)
		f.close()
	else :
		print "No such File"
def print_ver(filename,version):
	if os.path.isfile(filename) :
		f1 = open("curr.txt","w+")
		f1.truncate()
		f1.close()
		f2 = open(filename+"_buff","r")
		count = sum(1 for line in f2)
		f2.close()
		f2 = open(filename+"_buff","r")
		x = f2.readlines()
		i = 0
		if int(version) > int(count) :
			version = count
		while version > 0 :
			w = x[i].split()
			if w[0] == "0" :
				f1 = open("curr.txt","a")
				f1.write(w[1]+"\n")
				f1.close()
			else :
				f = open("curr.txt","r+")
				d = f.readlines()
				f.seek(0)
				for k,j in zip(range(len(d)),d):
	    				if k != int(w[0]) - 1:
						f.write(j)
				f.truncate()
				f.close()
			i = i+1
			version = int(version) - 1
		f2.close()
		f1 = open("curr.txt","r")
		file_contents = f1.read()
		print (file_contents)
		f1.close()
	else : 
		print "No such File"
def version_append(filename,characters):
	f = open(filename + "_buff","a")
	f.write("0 " + characters + "\n")
	f.close()
	f = open(filename + "_buff","r")
	count = sum(1 for line in f)
	f.close()
	f = open("log.txt","a")
	f.write(filename+" Version "+str(count)+" created at " + strftime("%Y-%m-%d %H:%M:%S")+"\n")
	f.close()
	f = open(filename,"a")
	f.write(characters + "\n")
	f.close()
def version_del(filename,dell):
	if os.path.isfile(filename + "_buff") :
		f = open(filename + "_buff","a")
		f.write(dell + "\n")
		f.close()
		f = open(filename + "_buff","r")
		count = sum(1 for line in f)
		f.close()
		f = open("log.txt","a")
		f.write(filename + " Version "+str(count)+" created at " + strftime("%Y-%m-%d %H:%M:%S")+"\n")
		f.close()
		f = open(filename,"r+")
		d = f.readlines()
		f.seek(0)
		for k,j in zip(range(len(d)),d):
			if k != int(dell) - 1:
				f.write(j)
		f.truncate()
		f.close()
	else :
		print "No File to delete Contents"
def revert_back(filename,version) :
	if os.path.isfile(filename + "_buff") :
		f1 = open("curr.txt","w+")
		f1.truncate()
		f1.close()
		f2 = open(filename+"_buff","r")
		count = sum(1 for line in f2)
		f2.close()
		f2 = open(filename+"_buff","r")
		x = f2.readlines()
		i = 0
		if int(version) > int(count) :
			version = count
		#print version
		while version > 0 :
			w = x[i].split()
			if w[0] == "0" :
				f1 = open("curr.txt","a")
				f1.write(w[1]+"\n")
				f1.close()
			else :
				f = open("curr.txt","r+")
				d = f.readlines()
				f.seek(0)
				for k,j in zip(range(len(d)),d):
	    				if k != int(w[0]) - 1:
						f.write(j)
				f.truncate()
				f.close()
			i = i+1
			version = int(version) - 1
		f2.close()
		f1 = open(filename+"_buff","w")
		f1.write("")
		f1.close()
		f1 = open(filename+"_buff","a")
		#print i
		for j in range(i) :
			f1.write(x[j])
		f1.close()
		f1 = open("curr.txt","r")
		file_contents = f1.read()
		print (file_contents)
		f1.close()
		f = open(filename,"w")
		f.write(file_contents)
		f.close()
		
	else :
		print "No File to Revert Back"
		

while(1) :
	ip = raw_input().split()
	if ip[1] == "-h" :
		print "svc 'filename' -option\n-v 'v' : To know version v of 'filename'\n-a 'characters' : To append 'characters' to 'filename'\n-d 'number' : To delete line 'number' from 'filename'\n-r 'v' : To revert back to version v\n"
	elif len(ip) == 2 :
		print_latest_version(ip[1])
	elif ip[2] == "-v" :
		print_ver(ip[1],ip[3])
	elif ip[2] == "-a" :
		version_append(ip[1],ip[3])
	elif ip[2] == "-d" :
		version_del(ip[1],ip[3])
	elif ip[2] == "-r" :
		revert_back(ip[1],ip[3])
	else :
		print "See 'svc -h' for correct syntax"
