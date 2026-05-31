# 个性化问候语：输入姓名和年龄，输出格式化问候
# Week 1 练习作业 - claude-camp

def generate_greeting(name, age):
    """根据年龄生成不同的问候语"""
    if age < 18:
        stage = "少年"
        wish = "好好学习，天天向上！"
    elif age < 30:
        stage = "青年"
        wish = "青春正好，努力追梦！"
    elif age < 60:
        stage = "中年"
        wish = "事业有成，家庭幸福！"
    else:
        stage = "长者"
        wish = "身体健康，福如东海！"
    
    return f"""
╔══════════════════════════════╗
  你好，{name}！
  你今年 {age} 岁，正值{stage}时期。
  祝你：{wish}
╚══════════════════════════════╝"""

def main():
    print("=== 个性化问候语生成器 ===")
    name = input("请输入你的姓名：")
    age = int(input("请输入你的年龄："))
    print(generate_greeting(name, age))

if __name__ == "__main__":
    main()