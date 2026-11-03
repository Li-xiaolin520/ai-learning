name = input("请输入你的名字：")
score = float(input("请输入你的成绩（0-100）"))

if score >= 90:
    print(f"你好 {name},你的成绩是优秀！")
elif score >= 60:
    print(f"你好 {name},你的成绩是及格，继续加油。")
else:
    print(f"你好 {name},很已憾，你需要准备补考了。")
