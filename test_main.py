import pytest
from main import display_help, fill_db, clear_db, process_digits

def test_help() :
    assert display_help()

def test_fill() :
    assert 0 < fill_db() <= 5000

def test_clear() :
    assert clear_db() == 0

@pytest.mark.parametrize('digits, return_code',[('3',0),('ff',13),('',13),('1234567890123',12)])
def test_process_nodb(digits,return_code) :
    clear_db()
    assert process_digits(digits) == return_code

def test_process_db() :
    fill_db()
    assert process_digits('123') == 0
    assert 0 < process_digits('3') <= 10
    assert 0 <= process_digits('3806742') <= 10