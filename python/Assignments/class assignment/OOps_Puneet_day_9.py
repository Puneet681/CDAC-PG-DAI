from abc import ABC,abstractmethod
class person:
    count =  0
    def __init__ (self,etype = '', name ='', mob = ''):
        person.count = person.count +1
        self.pid = etype+str(person.count)
        self.name = name
        self.mob = mob
    
    def set_pid (self,pid):
        self.pid = pid
    
    def set_name (self,name):
        self.name = name
        
    def set_mob (self,mob):
        self.mob = mob
        
    def get_pid (self,pid):
        return self.pid
    
    def get_name (self,name):
        return self.name
        
    def get_mob (self,mob):
        return self.mob
        
    def __str__ (self):
        return f"{self.pid} , {self.name}, {self.mob}"
    
class Emp(person,ABC):
    
    
    def __init__ (self,etype = '', name ='', mob = '', dt ='',ds = '' ):
        super().__init__ (etype,name, mob)
        self.dt = dt
        self.ds = ds
    
    @abstractmethod
    def cal_sal(self):
        pass
    def set_dt (self,dt):
        self.dt = dt
    
    def set_ds (self,ds):
        self.ds = ds
        
        
    def get_dt (self,dt):
        return self.dt
    
    def get_ds (self,ds):
        return self.ds
        
        
    def __str__ (self):
        return super().__str__()+f"{self.dt} , {self.ds}"
    
class cat_Emp(Emp):
    def __init__ (self, name ='', mob = '', dt ='',ds = '' , ch = '' , hrs = ''):
        super().__init__('c', name, mob, dt,ds)
        self.ch = ch
        self.hrs = hrs
    
    def set_ch (self,ch):
        self.ch = ch
    
    def set_hrs (self,hrs):
        self.hrs = hrs
        
        
    def get_ch (self,ch):
        return self.ch
    
    def get_hrs (self, hrs):
        return self.hrs
        
        
    def __str__ (self):
        return super().__str__()+f"{self.ch} , {self.hrs}"
    
    def cal_sal(self):
        return self.ch
    
class sal_Emp(Emp):
    def __init__ (self, name ='', mob = '', dt ='',ds = '' , sal = ''):
        super().__init__('c', name, mob, dt,ds)
        self.sal = sal
        self.bonus = int(sal)*0.1
    
    def set_sal (self,sal):
        self.sal = sal
    
    def set_bonus (self,bonus):
        self.bonus = bonus
        
        
    def get_sal (self,sal):
        return self.sal
    
    def get_bonus (self, bonus):
        return self.bonus
    
    
        
        
    def __str__ (self):
        return super().__str__()+f"{self.sal} , {self.bonus}"
    
    def cal_sal(self):
        return self.bonus
    
    

c = cat_Emp("Puneet", "454654","hr","ds","200","100")
print(c)
s = sal_Emp("Puneet","9689322681","hf","gdsyjfg","56468")
print(s)

print(c.cal_sal())
print(s.cal_sal())
