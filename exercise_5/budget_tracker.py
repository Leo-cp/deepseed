from datetime import datetime 
budget_data={}
budget_limits={
    "food":500,
    "transport":200,
    "entertainment":150,
}
def add_entry(month,category_type, category,amount):
    try:
        datetime.datetime.strptime(month,"%Y-%m")
    except ValueError:
        print("Invalid date format. use YYYY-MM.")
        return
    if month not in budget_data:
        budget_data[month]={"income":{},"expenses":{}}
    if category not in budget_data[month][category_type]:
        budget_data[month][category_type][category]=0
    budget_data[month][category_type][category] += amount
    print(f"added{amount} to {category_type}-{category} for {month}")
def show_summary(month):
    if month not in budget_data:
        print("No data for this month.")
        return
    data = budget_data[month]
    income_total=sum(data["income"].values())
    expenses_total=sum(data["expenses"].values())
    print(f"\n---Summary for {month}---")
    print(f"Total income: {income_total}")
    print(f"Total expenses: {expenses_total}")
    print(f"Balance: {income_total - expenses_total}")

    print("\n Expenses Breakdown")
    for category, amount in data["expenses"].items():
        warning=""
        if category in budget_limits and amount > budget_limits[category]:
            warning = "over budget"
        print(f"{category}:{amount} {warning}")
def show_trend():
    print("\n---Spending Trend---")
    for month in sorted(budget_data.keys()):
        expenses_total =sum(budget_data[month]["expenses"].values())
        print(f"{month}: {expenses_total}")
def export_summary():
    print("\n---Exporting Monthly Summary---")
    for month in sorted(budget_data.keys()):
        show_summary(month)
while True:
    print("\n===Personal Budget Tracker===")
    print("1. add income")
    print("2. add expenses")
    print("3. view monthly summary")
    print("4. show spending trend")
    print("5. export summary")
    print("6. exit")
    choice=input("choose an option")
    if choice=="1":
        m=input("enter month(YYYY-MM):")
        c=input("Enter income category:")
        try:
            a=float(input("Enter amount"))
            add_entry(m, "income",c,a)
        except ValueError:
            print("value must be a number")
    elif choice =="2":
        m=input("enter month(YYYY-MM):")
        c=input("Enter expenses category:")
        a=float(input("Enter amount"))
        add_entry(m, "expenses",c,a)
    elif choice =="3":
        m=input("Enter month(YYYY-MM):")
        show_summary(m)
    elif choice =="4":
        show_trend()
    elif choice =="5":
        export_summary()
    elif choice =="6":
        print("Goodbye")
        break
    else:
        print("invalide option.")