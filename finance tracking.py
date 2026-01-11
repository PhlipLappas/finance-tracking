import csv
import os
from datetime import datetime
import os
home = os.path.expanduser("~")
def ask_date(prompt="Date (YYYY-MM-DD): "):
        while True:
            s = input(prompt).strip()
            try:
                return datetime.strptime(s, "%Y-%m-%d").date()
            except ValueError:
                print("❌ That date does not seem to exist. Try something like: 2026-01-06")


def add_transaction():
    incomes = 0
    outcomes = 0
    date_value = ask_date()
    ttype = str(input('Outcome or Income?')).strip().lower()
    if ttype == 'outcome':
            category = str(input('What did you spend your money on?'))
    else:
            category = "income"
    amount = float(input("What is the amount?"))
    while amount < 0:
        amount = float(input("What is the amount?(Try something higher than 0)"))
    file = "transactions.csv"
    fields = ["date","type","category","amount"]
    file_exists = os.path.isfile(file)
    with open(file, mode="a",newline="",encoding="utf-8")as f:
        writer = csv.DictWriter(f,fieldnames=fields)

        if not file_exists:
            writer.writeheader()
    row = { 
        "date": date_value.isoformat(),
        "type": ttype,
        "category":category,
        "amount":amount
    }
    with open(file, mode="a",newline="",encoding="utf-8")as f:
        writer = csv.DictWriter(f,fieldnames=fields)
        writer.writerow(row)
    print("Transaction saved✅")
year = "2026"
month = "01"
target = year + "-" + month
valid = [ 
    'January',
    "February",
    "March"
]
MONTH_MAP = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
def month_summary():
    valid = [ 
    'January',
    "February",
    "March"
    ]
    MONTH_MAP = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

    year = "2026"
    month = input("Which month do you want to see the summary of?")
    while month not in valid:
        month = input("This month is not yet included. Please choose another one!")
    target = year + "-" + MONTH_MAP[month]
    incomes = 0
    outcomes = 0
    with open("transactions.csv",mode="r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("The outcomes of this month💰")
        rows = list(reader)
        for row in rows:
        
            if row["date"].startswith(target):
                amt = float(row["amount"])
              
                if row['type'] == "outcome":
                
                    print(row["amount"],"€",row["category"])
                    outcomes += amt
    print("The subtotal is:",outcomes,"€") 
            
    print("The incomes of this month💰")
    for row in rows:
        
        if row["date"].startswith(target):
            amt = float(row["amount"])
            
            if row['type'] == "income":
                
                print(row["amount"],"€",row["category"])
                incomes += amt
    print("The subtotal is:",incomes,"€")
    net = incomes-outcomes
    print("💰This months net is:",net,'€')
    if net > 0:
        print("You earned",net,"€ this month")
    elif net < 0:
        print("You lost",abs(net),"€ this month")
    else:
        print("You neither earned nor lost any money this month")
def show_month_transactions():
    with open("transactions.csv",mode="r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        for row in rows:
          if row["date"].startswith(target):
              print(row["date"],row["category"],row["amount"],"€")   
totals = {}

def category_breakdown():
    total_amount = 0
    with open("transactions.csv",mode="r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        for row in rows:
            if row["date"].startswith(target):
                if row["type"] == 'outcome':
                    cat = row["category"]
                    amnt = float(row["amount"])
                    
                    totals[cat] = totals.get(cat, 0) + amnt
                    sorted_totals = sorted( 
                        totals.items(),
                        key=lambda x: x[1],
                        reverse=True
                        )
                    total_amount+=amnt   
    
    print("💸Category breakdown:")
    for cat, total in sorted_totals:
        print(cat, "→", total, "€",round((total/total_amount)*100,2),"%")

def next_month_prediction():
     
     totals_months = {}
     totals_months2 = {}
     
     y = []
     
     with open("transactions.csv",mode="r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
                
            if row['type'] == "income":
                continue
                    
            month_key = row['date'][:7]
            amt = float(row['amount'])
            
            totals_months[month_key] = totals_months.get(month_key,0)+amt
        
        months = sorted(totals_months.keys())
        values = list(totals_months.values())
        last_3_values = values[-3:]
        y.extend(last_3_values)
        x = list(range(len(y)))
        
        trend = ((y[len(y)-1]-y[len(y)-2])+(y[len(y)-2]-y[len(y)-3]))/2
        y_pred = sum(y)/len(y)-trend
        next_month = len(y)+1
     MONTH_MAP = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
     }
     print("In",MONTH_MAP[str(next_month)],'your outcomes are probably going to be:',y_pred,"€")
                        

            
        
       

        

    


z = input("Hello! Do yo need any help for today?(yes/no)")             
while z == "yes":
    option = input("Would you like to see:1(add transaction),2(month summary),3(show month transactions),4(category_breakdown):")
    valid = [ 
    "1",
    "2",
    "3",
    "4",
    "5"
    ]
    while option not in valid:
        option = input("How can i help you today?[1(add transaction),2(month summary),3(show month transactions),4(category breakdown),5(next month prediction)]:")
    if option == "1":
        add_transaction()
    elif option =="2":
        month_summary()
    elif option == "3":
        show_month_transactions()
    elif option == "4":
        category_breakdown()
    else:
        next_month_prediction()
    z = input("Do yo need any help for today?(yes/no)")

print("Thanks for using our finance tracking system!")

