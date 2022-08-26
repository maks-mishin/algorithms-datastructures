def SynchronizingTables(N, ids, salary):
    sorted_ids, sorted_salary = sorted(ids), sorted(salary)

    correct_map_id_salary = {}
    for i in range(N):
        correct_map_id_salary[sorted_ids[i]] = sorted_salary[i]

    correct_salary = []
    for id_worker in ids:
        correct_salary.append(correct_map_id_salary[id_worker])
    return correct_salary
