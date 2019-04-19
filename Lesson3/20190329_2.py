def print1(*x):

	for i in range(7):
		if i < 4:	
			for m in range(len(e)):
				if m == 0:
					if i == 0:
						print ((6-i)*' '+e[m]+(3-i)*' ',end='')
					else :
						print ((6-i)*' '+e[m]+(2*i-1)*' '+ e[m] +(3-i)*' ',end='')
				else:
					if i == 0:
						print (3*' '+e[m]+3*' ',end='')
					else :
						print ((3-i)*' '+e[m]+(2*i-1)*' '+ e[m] +(3-i)*' ',end='')
			print('')
		else:
			for m in range(len(e)):
				if m == 0:
					print ((6-i)*' '+e[m]+6*' '+ e[m+1]+(i-4)*' ',end='')
				elif  m == len(e)-1 :
					print ((i-4)*' '+ e[m-1]+6*' '+e[m],end='')
				else :
					print ((i-4)*' '+e[m-1]+ (13-2*i)*' '+e[m+1]+(i-4)*' ',end='')
			print('')
	
	for i in range(1,7):
		if i < 3:
			for m in range(len(e)):
				if m == 0:
					print (i*' '+e[m]+6*' '+e[m+1]+(2-i)*' ',end='')
				elif m == len(e)-1:
					print ((2-i)*' '+e[m-1]+6*' '+e[m],end='')
				else :
					print ((2-i)*' '+e[m-1]+(2*i+1)*' '+ e[m+1] +(2-i)*' ',end='')
			print('')
		else:
			for m in range(len(e)):
				if m == 0:
					if i == 6:
						print (6*' '+e[m]+(i-3)*' ',end='')
					else:
						print (i*' '+e[m]+(11-2*i)*' '+e[m]+(i-3)*' ',end='')
				else:
					if i == 6:
						print ((i-3)*' '+e[m]+(i-3)*' ',end='')
					else:
						print ((i-3)*' '+e[m]+(11-2*i)*' '+e[m]+(i-3)*' ',end='')					
			print ('')
		

	





while 1 :     #程序一直运行
	
	e = list(input("请输入字符"))
	
	
	print1(e)