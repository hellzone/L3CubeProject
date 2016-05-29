while(1) :
	ip = raw_input().split()
	if ip[1].isdigit() :
		f1 = open("curr.txt","w+")
		f1.truncate()
		f1.close()
		f2 = open("filename_buff","r")
		x = f2.readlines()
		i = 0
		while ip[1] > 0 :
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
			ip[1] = int(ip[1]) - 1
		f2.close()
		f1 = open("curr.txt","r")
		file_contents = f1.read()
		print (file_contents)
		f1.close()
	else :
		f = open("filename_buff","a")
		print "1. Append at the end of file \n2. Delete any existing line"
		choice = input()
		if choice == 1 :
			app = raw_input()
			f.write("0 " + app + "\n")
			f.close()
			f = open("filename","a")
			f.write(app + "\n")
			f.close()
		else :
			print "Enter the line number you want to delete"
			dell = raw_input()
			f.write(dell + "\n")
			f.close()
			f = open("filename","r+")
			d = f.readlines()
			f.seek(0)
			for k,j in zip(range(len(d)),d):
    				if k != int(dell) - 1:
        				f.write(j)
			f.truncate()
			f.close()
