import employee_info as eInfo

def test_calculate_aerage_salary():
    employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 5},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 10},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 10},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 15},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 10},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 10}
    ]
    res_avg, res_total = eInfo.calculate_average_salary(employee_data)

    assert (res_avg == 10)
    assert (res_total == 60)