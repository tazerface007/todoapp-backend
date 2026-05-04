import pytest
from app.database import db_path

def test_currentdir():
    result = db_path
    print(f'Result: {result}')
    assert result