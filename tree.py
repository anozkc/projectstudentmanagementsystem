import pytest
@pytest.fixture()

def main():
    student_name = "anoj"
    student_location = "Banasthali"
    student_gender = "male"
    student_id  = 11
    return [student_name,student_location,student_gender,student_id]

def test_1(main):
    name = "anoj"
    assert main[0] == name

def test_2(main):
    location = "banasthali"
    assert main[1] == location

def test_3(main):
    gender = "male"
    assert main[2] == gender

def test_4(main):
    id = 11
    assert main[3]==id