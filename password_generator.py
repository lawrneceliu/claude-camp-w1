# 简单密码生成器：用户输入长度，生成随机字符串密码
# Week 1 练习作业 - claude-camp

import random
import string

def generate_password(length):
    """生成指定长度的随机密码"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(length):
    """评估密码强度"""
    if length < 6:
        return "弱 ⚠️"
    elif length < 10:
        return "中 👍"
    else:
        return "强 💪"

def main():
    print("=== 随机密码生成器 ===")
    length = int(input("请输入密码长度（建议8-16位）："))
    
    if length < 1:
        print("密码长度至少为1位！")
        return
    
    password = generate_password(length)
    strength = check_strength(length)
    
    print(f"""
生成的密码：{password}
密码长度：{length} 位
密码强度：{strength}
""")

if __name__ == "__main__":
    main()