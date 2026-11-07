#1.定义函数：接收一个文件路径，返回文件内容
#C++里可能是string read_file(string a){...}
#语法:def 函数名(参数名):
def read_knowledge_base(a):
    #函数名
    print(f"正在读取文件：{a}...")
    try:
        #with open 可以自动关闭，encodinh="utf-8"解决中文乱码
        #"r"代表read(只读模式)
        with open(a,"r",encoding="utf_8") as f:
            content = f.read()#文件内容全读成字符串
        return content
    except FileNotFoundError:
        #捕获异常，如果文件不存在，给个提示（try-catch)
        return"错误：找不到这个文件，请检查路径！"

#2.调用函数
file_path = "knowledge.txt"
text_content = read_knowledge_base(file_path)

#3.处理结果
if "错误" not in text_content:
    print("\n---知识库读取成功---")
    print(text_content)

    #算一下字数（len算字符串长度）
    char_count = len(text_content)
    print(f"\n该知识库共有{char_count}个字符。")
else:
    print(text_content)