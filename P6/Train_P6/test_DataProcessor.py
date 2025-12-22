from typing import List
import logging
import pytest

class EmpytDataError(Exception):
    pass

class DataProcessor:

    def __init__(self,data):
        self.data = data
        self.process = "In process"

    def process__data(self,data: List[int]) -> float:
        logging.info(f"Processing {len(self.data)} items")
        if not data:
            raise EmpytDataError("List cannot be empty")
        avg = sum(data) / len(data)
        return avg

def test_DataEmpty():
    db = DataProcessor([])
    
    with pytest.raises(EmpytDataError):
        db.process__data([])
        
    


    
        
