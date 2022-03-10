from connectpostgress import *


def Task1(sqlquery):
    data = cur.execute(sqlquery)
    records = cur.fetchall()
    list1 = []
    list2 = []
    list3 = []

    for i in records:
        temp_list = list(i)
        list1.append(temp_list[0])
        list2.append(temp_list[1])
        list3.append(temp_list[2])

    df = pd.DataFrame({'Employee Number': list1, 'Employee Name': list2, 'Manager Name': list3})
    writer = pd.ExcelWriter('/Users/somalayashwanthreddy/Downloads/q1.xlsx')
    df.to_excel(writer, sheet_name='Q1', index=False)
    writer.save()
    print('sucessful')






sqlquery = "select employee1.empno as employee_number, employee1.ename as employee_name, employee2.ename as manager_name " \
           "from emp employee1 inner join emp employee2 on employee1.mgr = employee2.empno "

Task1(sqlquery)





