#建一个空字典
student_scores={}

print("===欢迎使用班级成绩录入系统===")
print("(输入q退出录入)")

#循环
while True:
    name=input("\n请输入学生姓名：")
    if name=='q' or  name=="Q":
        print("退出录入...")
        break

    score_str=input(f"请输入{name}的成绩：")
    score = float(score_str)

    #字典名[键]=值
    student_scores[name]=score
    print(f"录入成功！当前已录入{len(student_scores)}人。")
print(f"\n---录入结束，开始统计---")

if len(student_scores)>0:
    total_score = sum(student_scores.values())
    average_score = total_score/len(student_scores)

    for name,score in student_scores.items():
        print(f"学生{name}:成绩{score}分")

    print(f"\n全班平均分：{average_score:.1f}分")
else:
    print("空")