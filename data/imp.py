import numpy as np
l=0.138
r=0.122


R1=np.array([200,550,150])
R2=np.array([200,600,100])

t1=np.array([2.2, 4.3, 4.8, 6.8])
t2=np.array([2.4, 4.1, 5, 6.6])

t1=t1*50*10**(-6)
t2=t2*50*10**(-6)



def s(R):
	R=R/1000
	R=R+np.array([l,0,r])
	r1=R[0]
	r2=R[1]
	r3=R[2]

	s1=r2
	s2=r2+2*r3
	s3=2*r1+r2
	s4=2*r1+r2+2*r3

	s=np.array([s1,s2,s3,s4])
	return s


print(s(R1)/t1)
ds=s(R2)-s(R1)
# print(s(R1))
# print(s(R2))
dt=t2-t1
print(ds/dt)