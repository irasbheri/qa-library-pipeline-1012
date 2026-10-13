"""Tests for validation.py.

TODO: Implement this test once validate_isbn is implemented in
src/data_processing/validation.py.
"""

from data_processing.validation import validate_isbn

def test_valid_isbn():
    result = validate_isbn('9780306406157')
    assert result == '9780306406157'

def test_valid_isbn_with_dashes():
    result = validate_isbn('-9780-30-640-61-57-')
    assert result == '9780306406157'

def test_invalid_isbn_with_dashes():
    result = validate_isbn('-90-30-6-6-57-')
    assert result is None

def test_invalid_isbn():
    result = validate_isbn('not-an-isbn')
    assert result is None

def test_wrong_length_too_short():
    result = validate_isbn('123')
    assert result is None

def test_wrong_length_too_long():
    result = validate_isbn('12345678921234567893123456789')
    assert result is None

def test_correct_length_but_letters():
    result = validate_isbn('ABCDEFGHIKLMN')
    assert result is None

def test_only_spaces():
    result = validate_isbn('   ')
    assert result is None

def test_special_characters():
    result = validate_isbn('!"£$%^&*()_+}')
    assert result is None
