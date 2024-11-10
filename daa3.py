class Item:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.value_per_weight=value/weight
    
    def __lt__(self,other):
        self.value_per_weight<other.value_per_weight

def knapsack(items,capacity):
    items.sort(reverse=True)
    total_value=0
    for item in items:
        if item.weight<=capacity:
            capacity-=item.weight
            total_value+=item.value
        else:
            fraction= capacity / item.weight
            total_value+=item.value * fraction
            break
    return total_value

def main():
    num_items=int(input("enter the number of items:"))
    items=[]
    for i in range(num_items):
        weight=float(input(f"enter the weight of the item {i+1}:"))
        value=float(input(f"enter the value of the item {i+1}:"))
        items.append(Item(weight,value))

    capacity = float(input("enter the capacity of the knapsack:"))

    total_value=knapsack(items,capacity)
    print(f"the total value of the knapsack is :{total_value:.2f}")

main()