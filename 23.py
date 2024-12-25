class complex:
    def__init__(self,tempReal,tempImaginary):
        self.real=tempReal
        self.imaginary=tempImaginary
    def addcomp(self,c1,c2):
        temp=complex(0,0)
        temp.real=c1.real+c2.real
        temp.imaginary=c1.imaginary+c2.imaginary
        return temp
if__name__=='__main__':
    c1=complex(3,2)
    print("complex number 1:",c1.real,"+i"+str(c1.imaginary))
    c2=complex(9,5)
    print("complex number 2:",c2.real,"+i"+str(c2.imaginary))
    c3=complex(0,0)
    c3=c3.addcomp(c1,c2)
    print("complex number 3:",c3.real,"+i"+str(c3.imaginary))