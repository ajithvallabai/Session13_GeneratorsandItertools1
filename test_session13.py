from session13 import NYCParking,NYCClassicParking
import math
import pytest
import os

README_CONTENT_CHECK_FOR = [    
    "yield",
    "iterator",
    "lazy properties",
    "data type",
    "violations"    
]

## Readme file - 2 test case

def test_readmeexists():
    assert os.path.isfile("README.md"), "README.md file missing!"
    print("Readme file exists")

def test_readmeproperdescription():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
    print("Readme file contains proper description")


def test_nyciterator():
    obj = NYCParking("nyc_parking_tickets_extract-1.csv")
    assert next(iter(obj)), "Please check your implementation"
    assert next(iter(obj)), "Please check your implementation"
    assert next(iter(obj)), "Please check your implementation"
    print("iterator is implemented with yield function")

def test_violations():
    obj = NYCParking("nyc_parking_tickets_extract-1.csv")
    assert obj.number_of_violations()["BMW"] == 11, "Please check your implementation"
    assert obj.number_of_violations()["CHEVR"] == 13, "Please check your implementation"
    assert obj.number_of_violations()["VOLVO"] == 2, "Please check your implementation"
    print("Datas of Violations are correct")

def test_nycclassiciterator():
    obj = NYCClassicParking("nyc_parking_tickets_extract-1.csv")    
    count = 0
    for _ in obj:
        count += 1
        pass    
    assert count == 1000, "Please check your implementation"
    print("list and forloop is implemented")
    











