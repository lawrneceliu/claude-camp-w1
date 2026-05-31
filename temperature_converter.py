# 温度转换器：摄氏度 ↔ 华氏度
# Week 1 练习作业 - claude-camp

def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    return (fahrenheit - 32) * 5 / 9

def main():
    print("=== 温度转换器 ===")
    print("1. 摄氏度 → 华氏度")
    print("2. 华氏度 → 摄氏度")

    choice = input("\n请选择转换方向（输入 1 或 2）：")

    if choice == "1":
        celsius = float(input("请输入摄氏度温度："))
        result = celsius_to_fahrenheit(celsius)
        print(f"\n{celsius}°C = {result:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("请输入华氏度温度："))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"\n{fahrenheit}°F = {result:.2f}°C")

    else:
        print("无效输入，请输入 1 或 2")

if __name__ == "__main__":
    main()