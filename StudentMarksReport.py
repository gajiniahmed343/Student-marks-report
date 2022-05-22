#StudentMarksReport.py
#validation of student number
while(True):
	sno=int(input("Enter Student Number(200-300):"))
	if(sno>=200) and (sno<=300):
		break
	print("Plz Enter Correct Student Number between 200 and 300")
#accept name of the student and college
sname=input("Enter Student Name:")
cname=input("Enter Student College Name:")
#validation of  C Marks
while(True):
	cm=int(input("Enter Marks in C(0-100):"))
	if(cm>=0) and(cm<=100):
		break
	print("Plz Enter C Marks within 0 to 100")
	
#validation of  CPP Marks
while(True):
	cppm=int(input("Enter Marks in CPP(0-100):"))
	if(cppm>=0) and(cppm<=100):
		break
	print("Plz Enter CPP Marks within 0 to 100")
#validation of  Python Marks
while(True):
	python=int(input("Enter Marks in PYTHON(0-100):"))
	if(python>=0) and(python<=100):
		break
	print("Plz Enter Python Marks within 0 to 100")

#cauculate total marks and percentage
totmarks=cm+cppm+python
percent=(totmarks/300)*100
#decide the grade  CM=60  CPPM=80   python 40
if((cm<40) or  (cppm<40) or (python<40)):
	grade="FAIL"
else:
	if (totmarks>=250) and  (totmarks<=300):
		grade="DISTINCTION"
	elif (totmarks>=200) and  (totmarks<=249):
		grade="FIRST"
	elif (totmarks>=150) and  (totmarks<=199):
		grade="SECOND"
	else:
		grade="THIRD"

#display student marks report
print("*"*50)
print("\tS t u d e n t  M a r k s  R e p o r t")
print("*"*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(sname))
print("\tStudent College Name:{}".format(cname))
print("\tStudent Marks in C: {}".format(cm))
print("\tStudent Marks in C++: {}".format(cppm))
print("\tStudent Marks in Python: {}".format(python))
print("-"*50)
print("\tStudent Total Marks: {}".format(totmarks))
print("\tStudent  Percentage of Marks: {}".format(percent))
print("\tStudent Grade: {}".format(grade))
print("*"*50)