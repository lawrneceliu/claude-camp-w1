# 小费计算器：输入餐费金额和小费比例，输出总金额
# Week 1 练习作业 - claude-camp

def calculate_tip(bill_amount, tip_percent, people=1):
    """计算小费和总金额"""
    tip_amount = bill_amount * tip_percent / 100
    total = bill_amount + tip_amount
    per_person = total / people
    return tip_amount, total, per_person

def main():
    print("=== 小费计算器 ===")
    
    bill = float(input("请输入餐费金额（元）："))
    tip_percent = float(input("请输入小费比例（%）："))
    people = int(input("请输入用餐人数："))
    
    tip, total, per_person = calculate_tip(bill, tip_percent, people)
    
    print(f"""
--- 账单明细 ---
餐费金额：¥{bill:.2f}
小费（{tip_percent}%）：¥{tip:.2f}
总金额：¥{total:.2f}
每人分摊：¥{per_person:.2f}
""")

if __name__ == "__main__":
    main()