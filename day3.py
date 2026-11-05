#字典
student_scores={
    "张三":85,
    "李四":95,
    "王五":58,
    "周六":72
}

print("---成绩单开始处理---")
#用for循环遍历字典
for name,score in student_scores.items():
    if score>=90:
        level="优秀"
    elif score>=60:
        level="及格"
    else:
        level="挂科"

    print(f"学生{name}:成绩{score}分,评级：{level}")
print("---所有成绩处理完毕---")

#sum()算数值总和；len()算长度/个数
#字典不能直接用sum,要用.values()提取出所有的分数
total_score=sum(student_scores.values())
student_count=len(student_scores)
average_score=total_score/student_count

print(f"全班平均分:{average_score:.1f}分")