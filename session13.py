import math 
from collections import namedtuple
import datetime

class NYCParking:
    """
    NYC Parking ticket iterator with yield operator
    """    
    def __init__(self,file_name):
        """
        :file_name :input file name
        :return :None
        """
        self.file = file_name        
        self.parking_index = 0
        self.information = []
        self.get_info(self.file)
        self.Ticket_header = self.form_named_tuple(self.information[0][1])
        self.total_length = len(self.information) -1
        

    def form_named_tuple(self, ticket_header):
        """
        :ticket_header :string
        :return :named tuple
        """
        ticket_headers = ticket_header.strip('\n').split(",")
        ticket_headers = [n.replace(" ","") for n in ticket_headers]
        Tickets = namedtuple("Tickets",ticket_headers)
        return Tickets

    def get_info(self, file_name):
        """
        :file_name :file name that has data
        :information : list of tickets
        """
        if len(self.information) == 0:
            with open(file_name, encoding='utf8', errors='ignore') as f:
                for i,ticket in enumerate(f):
                    self.information.append((i,ticket))
            return self.information
        else:
            return self.information

    def type_caste(self, data):
        """
        :data : list of string
        :return : type casting respective data type
        """
        data = int(data[0]), data[1],data[2], data[3], datetime.datetime.strptime(data[4],"%m/%d/%Y"), int(data[5]), data[6],data[7], data[8]
        return data
        
    def __iter__(self) -> 'list':  
        """ 
        :return class: generator
        """
        try:
            self.parking_index += 1
            for num in range(len(self.information)):
                tic_item = self.information[self.parking_index][1].split(",")
                tic_item[-1] = tic_item[-1].replace("\n","") 
                tic_item = self.type_caste(tic_item)
                yield self.Ticket_header(*tic_item)
        except:
            return None

    def number_of_violations(self):
        """
        :return : car_violation_dictionary with car names and violations made
        """
        car_violate_dict = dict()
        for num in range(len(self.information)):
            tic_item = self.information[num][1].split(",")
            tic_item[-1] = tic_item[-1].replace("\n","")

            if (tic_item[-1].find("VIOLATION") != -1):
                if tic_item[-2] not in car_violate_dict:
                    car_violate_dict[tic_item[-2]] = 1
                else:
                    car_violate_dict[tic_item[-2]] += 1     
        return car_violate_dict


    def __len__(self) -> 'int':
        """         
        :return length: int 
        """
        return self.total_length
    
    def __repr__(self) -> 'str':
        """         
        :return repr: string 
        """
        return "NYC Parking Sequence "
    
class NYCClassicParking:
    """
    NYC Parking ticket iterator with next operator
    """  
    def __init__(self,file_name):
        """
        :file_name :input file name
        :return :None
        """
        self.file = file_name        
        self.parking_index = 0
        self.information = []
        self.get_info(self.file)
        self.Ticket_header = self.form_named_tuple(self.information[0][1])
        self.total_length = len(self.information)
            
    def form_named_tuple(self, ticket_header):
        """
        :ticket_header :string
        :return :named tuple
        """
        ticket_headers = ticket_header.strip('\n').split(",")
        ticket_headers = [n.replace(" ","") for n in ticket_headers]
        Tickets = namedtuple("Tickets",ticket_headers)
        return Tickets

    def get_info(self, file_name):
        """
        :file_name :file name that has data
        :information : list of tickets
        """
        if len(self.information) == 0:
            with open(file_name, encoding='utf8', errors='ignore') as f:
                for i,ticket in enumerate(f):
                    self.information.append((i,ticket))
            return self.information
        else:
            return self.information

        
    def __iter__(self) -> 'list':  
        """              
        :return class: NYCIterator
        """
        #for i in self.information:
        #    yield i

        self.parking_index += 1       
        return self.NYCIterator(self.information, self.parking_index, self.Ticket_header)
    
    def __len__(self) -> 'int':
        """         
        :return length: int 
        """
        return self.total_length
    
    def __repr__(self) -> 'str':
        """         
        :return repr: string 
        """
        return "NYC Parking Sequence "
    
    class NYCIterator:
        def __init__(self, filecontent, parking_index, ticket_header) -> None:            
            self._content_obj = filecontent            
            self._index = 0            
            self.parking_index = parking_index
            self.ticket_header = ticket_header
        
        def __iter__(self):            
            return self
        
        def type_caste(self, data):
            """
            :data : list of string
            :return : type casting respective data type
            """
            data = int(data[0]), data[1],data[2], data[3], datetime.datetime.strptime(data[4],"%m/%d/%Y"), int(data[5]), data[6],data[7], data[8]
            return data

        def __next__(self):                       
            if self.parking_index >= len(self._content_obj):
                raise StopIteration
            else:
                index = self.parking_index                
                item = self._content_obj[index]
                self.parking_index += 1                
                item = item[1].split(",")
                item[-1] = item[-1].replace("\n","")
                item = self.type_caste(item)                
                return self.ticket_header(*item)
            
        
                