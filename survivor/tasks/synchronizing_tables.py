def SynchronizingTables(count: int, employee_numbers: list, employee_salaries: list) -> list:
    sorted_ids, sorted_salary = sorted(employee_numbers), sorted(employee_salaries)

    correct_map_id_salary = {}
    for i in range(count):
        correct_map_id_salary[sorted_ids[i]] = sorted_salary[i]

    correct_salary = []
    for id_worker in employee_numbers:
        correct_salary.append(correct_map_id_salary[id_worker])
    return correct_salary
