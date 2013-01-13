#!/usr/bin/env python
#script to calculate section properties - SI units
import inout
import math
def results(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11):
	inout.write_file(fn, "Moment of inertia X-X axis[cm^4]: ", Ix)
	inout.write_file(fn, "Moment of inertia Y-Y axis[cm^4]: ", Iy)
	inout.write_file(fn, "Area of section[cm^2]: ", A)
	inout.write_file(fn, "Section modulus X-X axis [cm^3]: ", Sx)	
	inout.write_file(fn, "Section modulus Y-Y axis [cm^3]: ", Sy)
	inout.write_file(fn, "Radius of gyration X-X axis [cm]: ", rx)
	inout.write_file(fn, "Radius of gyration Y-Y axis [cm]: ", ry)
	inout.write_file(fn, "Ixy [cm]: ", Ixy)
	inout.write_file(fn, "Ip [cm]: ", Ip)
	inout.write_file(fn, "xc [cm]: ", xc)
	inout.write_file(fn, "yc [cm]: ", yc)	
	return

print("Choose section type as follows:")
print("1- Angle Section (L)")
print("2-Pipe Section")
print("3-Hollow box")
print("4-Channel ('C', 'U')")
print("5-T shape")  
print("6-Equal I shape")
shape=inout.get_integer("Enter 1, 2, 3, 4, 5 or 6: ", 1)
if shape==1:
	print ("Calculating Angle (L) section")
	fname="angle.txt"
	b=inout.get_float("Length of the short leg (b) or '0' for 8cm: ", 8.0)
	t=inout.get_float("Thickness of the steel (t) or '0' for 1.5cm: ", 1.5)
	h=inout.get_float("Length of the long leg (d) or '0' for 10cm: ", 10.0)
	if h<b:
		print("Wrong input")
	else:
		a=b-t
		c=h-t
		x=(b**2+c*t)/(2*(b+c))
		y=(h**2+a*t)/(2*(b+c))
		A=(h-t)*t+b*t
		Ix=-t*(4*t**4-10*h*t**3-14*b*t**3+9*h*h*t*t+28*b*h*t**2+(b*t)**2-4*h**3*t-18*b*h*h*t+h**4+4*b*h**3)/(12*(t-h-b))
		Iy=-t*(t**4-2*h*t**3+(h**2)*(t**2)+4*b*h*t*t+6*b*b*h*t**2-6*b*b*h*t-4*t*b**3+4*h*b**3+b**4)/(12*(t-h-b))
		A=(h-t)*t+b*t
		Sx=Ix/(h-y)
		Sy=Iy/(b-x)
		rx=(Ix/A)**0.5
		ry=(Iy/A)**0.5
		Ixy="N/A"
		Ip="N/A"
		xc=-t*(t**2-h*t-b**2)/(2*((h-t)*t+b*t))
		yc=-((h-b)*t**2-h**2*t)/(2*((h-t)*t+b*t))
		fn=open(fname, 'a')
		results (Ix,Iy,A,Sx,Sy,rx,ry,Ixy,Ip,xc,yc)
		fn.close()
elif shape==2:
	print("Calculating Pipe Section")
	fname="pipe.txt"
	r=inout.get_float("Enter RADIUS of pipe or '0' for 8.8cm: ", 8.8)
	t=inout.get_float("Enter wall thickness of pipe or '0' for 4cm: ", 4.0)
	A=math.pi*(r**2-(r-t)**2)
	xc=0
	yc=0
	Ix=math.pi*(r**4-(r-t)**4)/4
	Iy=math.pi*(r**4-(r-t)**4)/4
	Ixy=0
	Ip=math.pi*(r**4-(r-t)**4)/2
	Sx=Ix/r
	Sy=Iy/r
	rx=(Ix/A)**0.5
	ry=(Iy/A)**0.5
	fn=open(fname, 'a')
	results (Ix,Iy,A,Sx,Sy,rx,ry,Ixy,Ip,xc,yc)
	fn.close()
elif shape==3:
	print ("Calculating Hollow Box")
	fname="hollow_box.txt"
	h=inout.get_float("Enter hight of Box or '0' for 10cm: ", 10)
	b=inout.get_float("Enter width of Box or '0' for 8cm: ", 8)
	t=inout.get_float("Enter wall thickness or '0' for 1.5cm: ", 1.5)
	A1=b*h
	Ix1=b*h**3/12
	Iy1=h*b**3/12
	Ixy1=0
	Ip1=b*h*(b**2+h**2)/12
	b1=b-t
	h1=h-t
	Ix2=b1*h1**3/12
	Iy2=h1*b1**3/12
	Ixy2=0
	A2=b1*h1
	Ixy2=0
	Ip2=b1*h1*(b1**2+h1**2)/12
	Ix=Ix1-Ix2
	Iy=Iy1-Iy2
	Ixy=0
	Ip=Ip1-Ip2
	Sx=Ix/(b/2)
	Sy=Iy/(h/2)
	A=A1-A2
	rx=(Ix/A)**0.5
	ry=(Iy/A)**0.5
	xc=0
	yc=0
	fn=open(fname, 'a')
	results (Ix,Iy,A,Sx,Sy,rx,ry,Ixy,Ip,xc,yc)
	fn.close()
elif shape==4:
	print("Caluclating Channel ('C', 'U') shape")
	fname="Channel.txt"
	D=inout.get_float("Input height of section or '0' for 15cm: ", 15.0)
	B=inout.get_float("Input flange length or '0' for 10cm: ", 10)
	tf=inout.get_float("Input thickness of flange or '0' for 1.5cm: ", 1.5)
	tw=inout.get_float("Input thickness of web or '0' for 1.5cm: ", 1.5)
	d=(D-2*tf)
	A=B*D- d*(B - tw)
	a1=(2*(B**2)*tf+D*(tw**2))/(2*B*D-2*D*(B - tw))
	a2=D/2
	Ix=((2*tf*(B**3)-(D-2*tf)*(tw**3))/12)+(2*B*tf*((B/2)-a1)**2)+(tw*(D-2*tf)*(a1-0.5*tw)**2)
	Iy=((B*D**3)-(B-tw)*(D-2*tf)**3)/12
	ry=(Iy/A)**0.5
	rx=(Ix/A)**0.5
	Sy=Iy/a2
	Sx=Ix/a1
	Zy=(D**2*tw / 4)+tf*(B-tw)*(D-tf)
	Ixy="N/A"
	Ip="N/A"	
	xc=((D-2*tf)*tw**2+2*B**2*tf)/(2*(D-2*tf)+2*B*tf)
	yc=tf+D/2
	fn=open(fname, 'a')
	results (Ix,Iy,A,Sx,Sy,rx,ry,Ixy,Ip,xc,yc)
	fn.close()
elif shape==5:
	print ("Calculating 'T' shape")
	fname="t_shape.txt"
	D=inout.get_float("Input height of shape or '0' for 25cm: ", 25)
	B=inout.get_float("Input length of the flange or '0' for 20cm: ", 20)
	tf=inout.get_float("Input thickness of the flange or '0' for 1.5cm: ", 1.5)
	tw=inout.get_float("Input thickness of the web or '0' for 1.0cm: ", 1)
	hw=D-tf
	A=B*tf+hw*tw
	xc=B/2
	yc=(hw**2*tw+D*tf**2+2*B*hw*tf)/(2*hw*tw+2*B*tf)
	Ix=(hw**4*tw**2+(4*B*hw*tf**3+6*B*hw**2*tf**2+4*B*hw**3*tf)*tw+B**2*tf**4)/(12*hw*tw+12*B*tf)
	Iy=hw*tw**3/12+tf*B**3/12
	Ixy="N/A"
	Ip="N/A"
	rx=(Ix/A)**0.5
	ry=(Iy/A)**0.5
	a2 = (B*tf**2+tw*D*(tf*2+D))/(B*tf*2+D* tw) 
	a1 = B/ 2
	Sx=Ix/a1
	Sy=Iy/a2
	fn=open(fname, 'a')
	results (Ix,Iy,A,Sx,Sy,rx,ry,Ixy,Ip,xc,yc)
	fn.close()
elif shape==6:
	print ("Calculating equal 'I' shape")
	fname="I_shape.txt"
	D=inout.get_float("Input height of shape or '0' for 25cm: ", 25)
	B=inout.get_float("Input length of flange or '0' for 15cm: ", 15)
	tf=inout.get_float("Input thickness of flange or '0' for 2cm: ", 2)
	tw=inout.get_float("Input thickness of the web or '0' for 2cm: ", 2)
	hw=D-2*tf
	A=hw*tw+2*B*tf
	xc=B/2
	yc=(2*tf+hw)/2
	Ix=(hw*tw**3+8*B*tf**3+12*B*hw*tf**2+6*B*tf*hw**2)/12
	Iy=hw*tw**3/12+tf*B**3/6
	Ixy="N/A"
	Ip="N/A"
	rx=(Ix/A)**0.5
	ry=(Iy/A)**0.5
	Sx=Ix/(0.5*B)
	Sy=Iy/(0.5*D)
	fn=open(fname, 'a')
	results (Ix,Iy,A,Sx,Sy,rx,ry,Ixy,Ip,xc,yc)
	fn.close()
else:
	print ("Wrong option!")