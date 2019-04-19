def print1(a,b,*x):
	r = (a + 1) // 2
	
	
	for i in range(1,r):
		if i < b+0.5:	
			for g in e:
				print ((r-i)*' '+(2*i-1)*g+(r-i)*' ',end='')
			print('')
		else:
			for g in e:
				print ((r-i)*' '+b * g + (2*(i - b)-1) * ' ' + b * g+(r-i)*' ',end='')
			print('')

	for i in range(r):
		if i < r-b-0.5:
			for g in e:
				print (i*' '+b*g+ (a-2*b-2*i)*' '+ b*g+i*' ',end='')
			print('')
		else:
			for g in e:
				print (i*' '+(a-2*i)*g+i*' ',end='')
			print('')





while 1 == 1:     #程序一直运行
	a = int(input("输入一个小于80的正奇数"))

	while a > 80:
		a= int(input("不在范围之内,请重新输入一个小于80的正奇数"))

	while a % 2 == 0:
		a = int(input("输入为偶数,请重新输入一个小于80的正奇数"))
	
	b = int(input("请输入一个小于第一个数的数"))

	while b >= a:
		b = int(input("请输入一个小于第一个数的数"))
		
	
	e = list(input("请输入符号"))
	
	
	print1(a,b,e)
	
    
