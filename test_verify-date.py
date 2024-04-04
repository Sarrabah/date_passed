import pytest
from verify_date import dateVerifier, DateServiceInterface

class TestDateService(DateServiceInterface):
    def get_current_date(self):
        current_date = [2024,4,4]
        return current_date

def test_if_the_date_is_passed_or_not() :
    current_date = TestDateService()
    date_verifier= dateVerifier(current_date)
    assert date_verifier.is_past("2024/04/23") == False


