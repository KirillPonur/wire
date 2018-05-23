#!/usr/bin/python
import numpy as np
l=0.138
r=0.122


R1=np.array([200,550,150])/1000+np.array([l,0,r])
R2=np.array([200,600,100])/1000+np.array([l,0,r])

t1=np.array([2.2, 4.3, 4.8, 6.8])
t2=np.array([2.4, 4.1, 5, 6.6])

t1=t1*50*10**(-6)
t2=t2*50*10**(-6)


def printnum(arr,precision):
	# print('\t'.join(map(str, arr)))
	def fmt(num,precision):
		f='{:0.'+str(precision)+'f}'
		return f.format(num)
	print('\t'.join(fmt(n,precision) for n in arr))

def printstr(arr):
	print('\tcolumns={'+(','.join(map(str, arr)))+'},')
	print('\t'.join(map(str, arr)))

def s(R):
	# R=R/1000
	# R=R+np.array([l,0,r])
	r1=R[0]
	r2=R[1]
	r3=R[2]

	s1=r2
	s2=r2+2*r3
	s3=2*r1+r2
	s4=2*r1+r2+2*r3

	s=np.array([s1,s2,s3,s4])
	return s

printstr(['r1','r2','r3'])
printnum(np.hstack([R1]),3)
printnum(np.hstack([R2]),3)

print()
printstr(['S1','S2','S3','S4'])
printnum(np.hstack([s(R1)]),3)
printnum(np.hstack([s(R2)]),3)

print()
printstr(['S1','S2','S3','S4'])
printnum(s(R1),3)
printnum(t1*1000000,1)
printnum(s(R1)/t1,2)

print()
printstr(['S1','S2','S3','S4'])
printnum(s(R2),3)
printnum(t2*1000000,1)
printnum(s(R2)/t2,2)

ds=s(R2)-s(R1)
dt=t2-t1
v=ds/dt
print()
printstr(['dS1','dS2','dS3','dS4'])
printnum(ds,3)
printnum(dt*1000000,1)
printnum(v,0)
# print(s(R1))
# print(s(R2))