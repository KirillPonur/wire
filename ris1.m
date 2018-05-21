rp=[
	0, 100,200,300,400,500,600,700
	];
Max=[
	5,5,4.6,5.1,4.8,5.3,5,4.7
	].*0.05;
Min=[
	2.4,2.8,3,4.2,4,5.4,5.1,6.3
	].*0.02;
y=Max./Min;
set(0,'defaultTextInterpreter','latex');
set(0,'DefaultAxesFontSize',12);
set(0,'DefaultTextFontSize',12);
hold on
grid minor 
grid on
pp=plot(rp,y,'r*');
pp=plot(fittedmodel);
xlabel('x')
ylabel('���')
saveas(pp,'plot.png')