# BMI 计算器：输入身高体重，输出 BMI 数值和健康建议
# Week 1 练习作业 - claude-camp

def calculate_bmi(weight, height):
    """计算 BMI 值"""
    return weight / (height ** 2)

def get_health_advice(bmi):
    """根据 BMI 给出健康建议"""
    if bmi < 18.5:
        category = "偏瘦"
        advice = "建议适当增加营养摄入，均衡饮食。"
    elif bmi < 24:
        category = "正常"
        advice = "体重正常，继续保持健康的生活方式！"
    elif bmi < 28:
        category = "偏胖"
        advice = "建议适当控制饮食，增加运动量。"
    else:
        category = "肥胖"
        advice = "建议咨询医生，制定合理的减重计划。"
    return category, advice

def main():
    print("=== BMI 计算器 ===")
    weight = float(input("请输入体重（kg）："))
    height = float(input("请输入身高（m，例如1.75）："))

    bmi = calculate_bmi(weight, height)
    category, advice = get_health_advice(bmi)

    print(f"""
--- 健康报告 ---
BMI 数值：{bmi:.1f}
健康状态：{category}
健康建议：{advice}
""")

if __name__ == "__main__":
    main()