with t1 as(select m.id from Employee e
join Employee m on e.managerId = m.id
group by m.id
having count(e.managerid)>4)
select Employee.name from Employee
join t1 on t1.id = Employee.id