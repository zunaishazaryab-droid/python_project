student1=88
student2=88
student3=88
studentmarks=[34,45,67,89,90]
print(studentmarks)
print(studentmarks[2])
print(len(studentmarks)-4)

studentname=["fatima","zunaisha","zakia","raziaa"]
print(studentname)
studentname[0]="noor"
print(studentname)
studentname.insert(4,"fatima")
print(studentname)
studentname.append("isha")
print(studentname)
studentname.extend(["aneeba","ayesha","zara"])
print(studentname)


row1=["$$","$$","$$"]
row2=["$$","$$","$$"]
row3=["$$","$$","$$"]
map=[row1,row2,row3]
print(map)
print(f"{row1}\n{row2}\n{row3}")
position=input("enter your position:first digit will be column and second digit will be row")
column_no=int(position[0])
row_no=int(position[1])
print(column_no)
print(row_no)
map[row_no-1][column_no-1]="x"
print(f"{map[0]}\n{map[1]}\n{map[2]}")

