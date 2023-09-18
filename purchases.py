num_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

count=num_purchases
names = []
costs = []        
while count>=1:
    customer_input = str(input("Customer: "))
    cost_input = int(input("Cost: "))
    names.append(customer_input)
    costs.append(cost_input)
    count -= 1

def add_tax(cost_list, sales_tax_value):
    cost_with_tax=[]
    sales_tax_value = sales_tax
    cost_list=costs
    for cost in cost_list:
        total = (cost * sales_tax_value) + cost
        cost_with_tax.append(total)
    return cost_with_tax

final_cost = add_tax(costs, sales_tax)

cost_per_customer = {}

counter=len(names) - 1
while counter>= 0:
    i=counter
    names_entry = names[i]
    cost_per_customer[names_entry] = "0"
    counter-=1

if len(cost_per_customer) < len(names):
    for i,person in enumerate(cost_per_customer):
        count=0
        value=0
        while count<len(names):
            if person == names[count]:
                value += final_cost[count]
                count += 1
                cost_per_customer[person]= value
            else:
                count += 1

print(cost_per_customer)
