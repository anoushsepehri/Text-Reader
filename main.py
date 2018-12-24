import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from PIL import Image, ImageOps
import user_functions as uf


img=input("Enter file to convert: ")

end_col,start_col,end_row,start_row=0,0,0,0
digits=[]

test=Image.open(img).convert('L')
test=ImageOps.invert(test)
w,h=test.size
pic=test.getdata()
pic=np.array(pic)
pic=pic.reshape(h,w)

data=np.array(pd.read_csv("train.csv"))

test_labels=data[0:42000,0]
test_num=data[0:42000,1:]

clf=DecisionTreeClassifier()
clf.fit(test_num,test_labels)


while True:
	start_row=uf.findstartrow(pic,h,w)
	start_col=uf.findstartcol(pic,h,w,end_col)

	if start_col==None:
		break

	end_row=uf.findendrow(pic,h,w,start_row)
	end_col=uf.findendcol(pic,h,w,start_col)

	if end_row-start_row<end_col-start_col:
		seg=((end_col-start_col)-(end_row-start_row))/2 +25
		end_row+=seg
		start_row-=seg
		end_col+=25
		start_col-=25
	
	else:
		seg=((end_row-start_row)-(end_col-start_col))/2 +25
		end_col+=seg
		start_col-=seg
		start_row-=25
		end_row+=25

	start_col,end_col,start_row,end_row=round(start_col),round(end_col),round(start_row),round(end_row)
	cropped_digit=pic[round(start_row):round(end_row),round(start_col):round(end_col)]
	cropped_digit= Image.fromarray(cropped_digit)
	cropped_digit=cropped_digit.resize([28,28])
	cropped_digit=np.array(cropped_digit).reshape(1,-1)

	digits.append(cropped_digit)


digits=np.array(digits)
x,y,z=digits.shape
digits=digits.reshape(x,y*z)

numbers_pred=clf.predict(digits)
numbers=''.join(map(str, numbers_pred))
uf.print_to_file(numbers)
print("Complete")



