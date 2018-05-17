import numpy as np
import matplotlib.pyplot as plt
# Измеряем период волны в непрерывном режиме
T4=7.9*1*10**(-6)
T=T4/4
print('Период волны, T=',T,' с')


# измеряем длину волны, перемещая катушки приемника по полуволновым пучностям, от 0 до 20 максимума
print('Длина волны, lambda=',(718-612)/10,' мм')
# l=np.array([792,787,782,777,772,766,761,755,750,745,740,734,728,723,718,713,])

# максимальная амплитуда в пучности
Imax=5.1*0.02
#минимальная амплитуда в узле
Imin=3.4*0.01
KSV=Imax/Imin
print('КСВ, =',KSV)




# как поставить фазовую пластинку в диагональное положение




l=0.138
r=0.122

ri=40/1000+l # (40=860)


rp=np.array([
	0, 100,200,300,400,500,600,700
	])
Max=np.array([
	5,5,4.6,5.1,4.8,5.3,5,4.7
	])*0.05
Min=np.array([
	2.4,2.8,3,4.2,4,5.4,5.1,6.3
	])*0.02
print(Max/Min)
plt.plot(rp,Max/Min)
plt.show()

# оба в центре
ri=350
rp=394
Imax=3.9*0.02
Imin=2*0.01
print(Imax/Imin)

# передатчик в центре, приемник справа
ri=350
rp=0
Imax=3.5*0.02
Imin=1*0.01
print(Imax/Imin)

# оба справа
ri=728
rp=0
Imax=3.9*0.05
Imin=1.9*0.02
print(Imax/Imin)




rp1=874
rp2=661
# drp=(rp1-rp2)/10
print('Длина волны вторым способом, lambda=',(rp1-rp2)/20,' мм')


# период максимумов при движении передающей катушки. Выставляем одну фазу

ri1=151
ri2=256
print('Период по излучателю ',(ri2-ri1)/10,' мм')

# R1=np.array([200,550,150])
# R2=np.array([200,600,100])

# t1=np.array([2.2, 4.3, 4.8, 6.8])
# t2=np.array([2.4, 4.1, 5, 6.6])

# t1=t1*50*10**(-6)
# t2=t2*50*10**(-6)



# def s(R):
# 	R=R/1000
# 	R=R+np.array([l,0,r])
# 	r1=R[0]
# 	r2=R[1]
# 	r3=R[2]

# 	s1=r2
# 	s2=r2+2*r3
# 	s3=2*r1+r2
# 	s4=2*r1+r2+2*r3

# 	s=np.array([s1,s2,s3,s4])
# 	return s


# print(s(R1)/t1)
# ds=s(R2)-s(R1)
# # print(s(R1))
# # print(s(R2))
# dt=t2-t1
# print(ds/dt)