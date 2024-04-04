import datetime
from abc import ABC, abstractmethod

    
class DateServiceInterface(ABC):
    @abstractmethod
    def get_current_date(self):
        ...

class DateService(DateServiceInterface):

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


class dateVerifier:

    def __init__(self, current_date: DateServiceInterface):
        self.current_date = current_date
    

    def is_past(self, given_date):

        is_past = False

        given_date_table = given_date.split("/")

        for i in range(len(given_date_table)):
            given_date_table[i] = int(given_date_table[i])
            
        if (given_date_table[1] >= 1 and given_date_table[1] <= 12 ) and (given_date_table[2] >= 1 and given_date_table[2] <= 31):
            for j in range(3):
                if given_date_table[j] != self.current_date.get_current_date()[j]:
                
                    if given_date_table[j] < self.current_date.get_current_date()[j]:
                        is_past = True
                        return is_past
        
        return is_past



current_date = DateService()
date_verifier = dateVerifier(current_date)
print(date_verifier.is_past("2024/04/23"))