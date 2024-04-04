import pytest
from verify_date import dateVerifier, Date

def test_if_the_date_is_passed_or_not() :
    current_date = Date()
    date_verifier= dateVerifier(current_date)
    assert date_verifier.is_past("2024/04/23") == False


