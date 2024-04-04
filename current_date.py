import datetime
from abc import ABC, abstractmethod

    
#la classe abstraite
class Os_Current_Date_Service(ABC):
    @abstractmethod
    def get_current_date(self):
        ...

#l'implémentation
class Os_Current_Date(Os_Current_Date_Service):

    def get_current_date(self): 
        current_date_table = []

        current_date_formatted = datetime.datetime.today().strftime ('%Y/%m/%d')
        
        for i in range(3):
            if i == 0 :
                current_date_table.append(int(current_date_formatted[0:4]))
            elif i == 1 :
                current_date_table.append(int(current_date_formatted[5:7]))
            elif i == 2 :
                current_date_table.append(int(current_date_formatted[8:10]))
    
        return current_date_table


class Is_Passed:

    def __init__(self, current_date: Os_Current_Date_Service):
        self.current_date = current_date
    

    def is_past(self, given_date):

        is_past = False

        given_date_table = given_date.split("/")

        for i in range(len(given_date_table)):
            given_date_table[i] = int(given_date_table[i])
        
        for j in range(3):
            if given_date_table[j] != self.current_date.get_current_date()[j]:
                
                if given_date_table[j] < self.current_date.get_current_date()[j]:
                    is_past = True
                    return is_past
        
        return is_past


#l'éxecution
current_date = Os_Current_Date()
x = Is_Passed(current_date)
print(x.is_past("2024/04/03"))