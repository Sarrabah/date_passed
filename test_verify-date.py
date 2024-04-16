import pytest
from verify_date import DateVerifier, DateServiceInterface

class TestDateService(DateServiceInterface):
    def get_current_date(self):
        current_date = [2024,4,4]
        return current_date

def test_if_the_date_is_passed() :
    current_date = TestDateService()
    date_verifier= DateVerifier(current_date)
    assert date_verifier.is_past("2024/04/2") == True

def test_if_the_date_is_not_passed() :
    current_date = TestDateService()
    date_verifier= DateVerifier(current_date)
    assert date_verifier.is_past("2024/04/23") == False

def test_when_we_give_the_same_date_of_the_fixed_current_date() :
    current_date = TestDateService()
    date_verifier= DateVerifier(current_date)
    assert date_verifier.is_past("2024/04/4") == False

def test_should_return_false_if_the_date_is_not_well_formated() :
    current_date = TestDateService()
    date_verifier= DateVerifier(current_date)
    assert date_verifier.is_past("12/3/2027") == False

def test_if_the_date_is_not_passed() :
    current_date = TestDateService()
    date_verifier= DateVerifier(current_date)
    assert date_verifier.is_past("") == False