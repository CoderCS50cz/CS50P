from project import function_1, function_2, function_n
import pytest


def test_function_1():
    assert function_1("SMALL Phone") == "Price for your phone is: 429"
    assert function_1("expensive") == "Price for your huge Phone is 999"
    assert function_1("cat") == "Price for your huge Phone is 999"
    assert function_1(0) == "Price for your huge Phone is 999"

    with pytest.raises(TypeError):
        function_1()


def test_function_2():
    assert function_2(999, 1, 8) == [{'Month': 1, 'Monthly Payment (in $)': 999.0, 'Balance of debt (in $)': 999, 'Monthly Interest Rate': '8.00%', 'Loan amount at interest (in $)': 79.92, 'Loan (in $)': 1078.92}]
    assert function_2(429, 3, 10) == [{'Month': 1, 'Monthly Payment (in $)': 143.0, 'Balance of debt (in $)': 429, 'Monthly Interest Rate': '3.33%', 'Loan amount at interest (in $)': 14.3, 'Loan (in $)': 157.3}, {'Month': 2, 'Monthly Payment (in $)': 143.0, 'Balance of debt (in $)': 286.0, 'Monthly Interest Rate': '3.33%', 'Loan amount at interest (in $)': 9.53, 'Loan (in $)': 152.53}, {'Month': 3, 'Monthly Payment (in $)': 143.0, 'Balance of debt (in $)': 143.0, 'Monthly Interest Rate': '3.33%', 'Loan amount at interest (in $)': 4.77, 'Loan (in $)': 147.77}]

    with pytest.raises(ZeroDivisionError):
        function_2(0, 0, 0)
    with pytest.raises(ZeroDivisionError):
        function_2(100, 0, 10)
    with pytest.raises(TypeError):
        function_2(100, 10)
    with pytest.raises(TypeError):
        function_2(100, 10, "cat")



def test_function_n():
    # For testing function_n() please change the date to output string with adding extra 14 days to your testing date and pytest will pass the tests.
    # For example if your are testing in current day January 10, 2024, change output testing function to 2024-01-24.
    assert function_n("ReGuLaR Phone") == 'This is a certificate for your new "ReGuLaR Phone". Validation only for 14 days till 2024-01-24.'
    assert function_n("huge Phone") == 'This is a certificate for your new "huge Phone". Validation only for 14 days till 2024-01-24.'
    assert function_n("cat") == 'This is a certificate for your new "cat". Validation only for 14 days till 2024-01-24.'
    assert function_n(0) == 'This is a certificate for your new "0". Validation only for 14 days till 2024-01-24.'

    with pytest.raises(TypeError):
        function_n()
