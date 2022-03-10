from connectpostgress import *


def Task2(sqlquery):
    cur.execute("UPDATE jobhist SET enddate=CURRENT_DATE WHERE enddate IS NULL;")
    data = cur.execute(sqlquery)
    records = cur.fetchall()
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []

    for i in records:
        temp_list = list(i)
        list1.append(temp_list[0])
        list2.append(temp_list[1])
        list3.append(temp_list[2])
        list4.append(temp_list[3])
        list5.append(temp_list[4])
        list6.append(temp_list[5])
        # print(temp_list)
    # print(c1)
    # print(c2)
    # print(c3)
    df = pd.DataFrame(
        {'Employee Name': list1, 'Employee No': list2, 'Dept Name': list3, 'Dept Number': list4, 'Total Compensation': list5,
         'Months Spent': list6})
    writer = pd.ExcelWriter('/Users/somalayashwanthreddy/Downloads/q2.xlsx')
    df.to_excel(writer, sheet_name='Q2', index=False)
    writer.save()
    print("Sucessful")



sqlquery="SELECT emp.ename, jobhist.empno, " \
            "dept.dname, jobhist.deptno, " \
            "ROUND((jobhist.enddate-jobhist.startdate)/30*jobhist.sal,0) AS total_compensation, " \
            "ROUND((jobhist.enddate-jobhist.startdate)/30,0) as months_spent " \
            "FROM jobhist  INNER JOIN dept ON jobhist.deptno=dept.deptno " \
            "INNER JOIN emp ON jobhist.empno=emp.empno;"

Task2(sqlquery)







