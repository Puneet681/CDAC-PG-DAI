# Telecom Company 
class ABCTel:
    def __init__(self,name = '',email = ''):
        self.__name = name
        self.__email = email
        
    def set_name (self,name):
            self.__name = name
    def set_email (self,email):
             self.__email = email
             
    def get_name (self):
            return self.__name
    def get_email (self):
            return self.__email
        
    def __str__(self):
        return f"name :- {self.__name} , email :-{self.__email} "
        
# Indvidual Customer 
class ind_cust(ABCTel):
    def __init__(self,name = '',email = '',phone = '',credit_class='',discount=0,plan=''):
        super().__init__(name,email)
        self.__phone = phone 
        self.__credit_class = credit_class 
        self.__discount = discount 
        self.__plan = plan 
    
    def set_phone (self,phone):
        self.__phone = phone 
    
    def set_discount (self,discount):
         self.__discount =discount
         
    
    def set_credit_class (self,credit_class):
        self.__credit_class = credit_class
    
    def set_plan (self,plan):
         self.__plan =plan
         
    
    def get_phone (self):
        return self.__phone
    
    def get_credit_class (self):
        return self.__credit_class
    
    def get_plan (self):
        return self.__plan
    
    def get_discount (self):
        return self.__discount
    
    def __str__(self):
        return super().__str__()+f"phone :- {self.__phone} ,credit_class :- {self.__credit_class},Discount :- {self.__discount} ,plan:- {self.__plan}"
    
# Compony Cust
class compy_cust(ABCTel):
    def __init__(self,name = '',email = '',rel_man={},cred_line='',extension='',lst_of_num=[]):
        super().__init__(name,email)
        self.__rel_man = rel_man
        
        self.__cred_line = cred_line
        
        self.__extension = extension
        
        self.__lst_of_num = lst_of_num
        
        
    def set_rel_man (self,rel_man):
        self.__rel_man = rel_man
    
    def set_cred_line (self,cred_line):
         self.__cred_line = cred_line
         
    def set_extension (self,extension):
        self.__extension = extension
    
    def set_lst_of_num (self,lst_of_num):
         self.__lst_of_num = lst_of_num
         
    def get_rel_man (self):
        return self.__rel_man
    
    def get_cred_line (self):
        return self.__cred_line
    
         
    def get_extension (self):
        return self.__extension
    
    def get_lst_of_num (self):
        return self.__lst_of_num
    
    def __str__(self):
        return super().__str__()+f"relationship manager :- {self.__rel_man} ,Credit_line :- {self.__cred_line},Extension :- {self.__extension} ,List of numbers :- {self.__lst_of_num}"
            
# Vendor
class vendor(ABCTel):
    def __init__(self,name = '',email = '',phone = '',list_of_prod=[]):
        super().__init__(name,email) 
        self.__phone = phone
        self.__list_of_prod = list_of_prod
        
    def set_phone (self,phone):
        self.__phone = phone
    def set_list_of_prod (self,list_of_prod):
         self.__list_of_prod = list_of_prod
         
    def get_phone (self):
        return self.phone
    def get_list_of_prod (self):
        return self.__list_of_prod
    
    def __str__(self):
        return super().__str__()+f"phone :- {self.__phone} ,list of Products :- {self.__list_of_prod} "
    
s = vendor("bsfgdj","gjkfd","jhkf",[123,213213,3213])
g = compy_cust('Ank','asdas',{'x':123},'A','NA',[21213123123,21321313123,123123123])
print(s)
print(g)
v = ind_cust("Puneet","jhhe","486486","A",45,"vip")
print(v)
    
        