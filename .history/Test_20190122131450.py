class Person:
    def _init_(self,name):
        self.name=name

        
    def sayhello(self):
        print ('My name is:',self.name)



        
p=Person('Bill')
print (p)