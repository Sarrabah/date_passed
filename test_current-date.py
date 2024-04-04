import pytest
from current_date import Is_Passed, Os_Current_Date

def test_if_the_date_is_passed_or_not() :
    curr = Os_Current_Date()
    ip = Is_Passed(curr)
    assert ip.is_past("2024/04/23") == False


