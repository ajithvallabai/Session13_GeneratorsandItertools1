### Session 13 - Generators and Itertools 1

Google Colab notebook - [here](https://colab.research.google.com/drive/1CCNAODxbF1GrQC_9RHcSgQIMLz7shFgU?usp=sharing)

**iter()**
```
self.parking_index += 1
for num in range(len(self.information)):
    tic_item = self.information[self.parking_index][1].split(",")
    tic_item[-1] = tic_item[-1].replace("\n","") 
    tic_item = self.type_caste(tic_item)
    yield self.Ticket_header(*tic_item)
```

Iter method is used to implement iterator with yield keyword. Here each line in the .csv file is taken and then processed and the fed as return when each time iterator is called. Not able to implement iterator properly so used NYCClassicParking method where next() is used


**Namedtuple**
```
def form_named_tuple(self, ticket_header):        
    ticket_headers = ticket_header.strip('\n').split(",")
    ticket_headers = [n.replace(" ","") for n in ticket_headers]
    Tickets = namedtuple("Tickets",ticket_headers)
    return Tickets
```
We have took the first line and removed the spaces in each word and then we have formed a named tuple

**Casting**
```
def type_caste(self, data):
    """
    :data : list of string
    :return : type casting respective data type
    """
    data = int(data[0]), data[1],data[2], data[3], datetime.datetime.strptime(data[4],"%m/%d/%Y"), int(data[5]), data[6],data[7], data[8]
    return data
```
We have casted each item in data to corresponding data type and then we are returning.

**number_of_violations()**
```
def number_of_violations(self):    
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
```

We are iterating and using a dictionary to store the information of violated cars name and its count in a lazy properties method

