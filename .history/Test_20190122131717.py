class Motor:
    '''Motor control'''
    def __init__(self,ENA):
        '''Specify motor pins'''
        self.enab_pin=[ENA,ENB] #Enable pins
        self.inx_pin=[IN1,IN2,IN3,IN4] #Control pins
        
        self.RightAhead_pin=self.inx_pin[3]
        self.RightBack_pin=self.inx_pin[2]
        self.LeftAhead_pin=self.inx_pin[1]
        self.LeftBack_pin=self.inx_pin[0]

        self.setup()


class Person:
    def _init_(self,name):
        self.name=name

        
    def sayhello(self):
        print ('My name is:',self.name)



        
p=Person('Bill')
print (p)