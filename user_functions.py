
def findstartrow(pixels,h,w):
	for i in range(0,h): 		#Passing through Rows
		for x in range(0,w): 	#Passing through Columns
			if pixels[i,x]!=0:
				return i

def findendrow(pixels,h,w,start):
	for i in range(start,h):
		count=0
		for x in range(0,w):
			if pixels[i,x]!=0:
				count+=1
		if count==0:
			return i

def findstartcol(pixels,h,w,start):
	for x in range(start,w): 		#Passing through Rows
		for i in range(0,h): 		#Passing through Columns
			if pixels[i,x]!=0:
				return x
				
def findendcol(pixels,h,w,start):
	for x in range(start,w):
		count=0
		for i in range(0,h):
			if pixels[i,x]!=0:
				count+=1
		if count==0:
			return x


def print_to_file(number):
	file=open('numbers.txt','w')
	file.write(number)
	file.close()