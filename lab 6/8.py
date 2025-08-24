class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __eq__(self, other):
    
           return(self.hour==other.hour and self.minute==other.minute and self.second==other.second) 
    def __str__(self):
        return f"{self.hour} {self.minute} {self.second}"
t1 = Time(10, 30, 45)
t2 = Time(10, 30, 45)
t3 = Time(12, 15, 0)
print(t1==t2)
print(t2==t3)
print(f'Time : {t1}')
print(f'Time : {t2}')
print(f'Time : {t3}')