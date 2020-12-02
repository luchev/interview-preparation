SELECT employee_id,
    team_size
FROM (
        SELECT team_id,
            COUNT(employee_id) as team_size
        FROM Employee
        GROUP BY team_id
    ) as employee_count
    JOIN Employee on Employee.team_id = employee_count.team_id
