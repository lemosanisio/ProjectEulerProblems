fibo = [1,2]
fiboe = []
while fibo[-1] <4*10**6:
	fibo.append(fibo[-1]+fibo[-2])
for i in fibo:
	if i%2==0:
		fiboe.append(i)
print(sum(fiboe))