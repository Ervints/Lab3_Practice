import employee_info as eInfo

def test_calculate_aerage_salary():
    result = eInfo.calculate_average_salary()

    assert (result == 60167)

def test_get_employee_by_dept():
    result = []
    department = "Marketing"
    
    result = eInfo.get_employees_by_dept(department)

    assert (result == [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}])

def test_employees_by_age_range():
    lowLimit = 25
    highLimit = 35
    result = []

    result = eInfo.get_employees_by_age_range(lowLimit, highLimit)

    assert (result == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}])

    #comment added to test git tag