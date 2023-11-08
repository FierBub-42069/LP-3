print('Iteration no.: (total_value, total_weight)')
def fractional_knapsack(items, capacity):
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    total_value = 0
    total_weight = 0
    i = 0

    for item in items:
        if total_weight + item[1] <= capacity:
            total_value += item[0]
            total_weight += item[1]
            i += 1
        else:
            fraction = (capacity - total_weight) / item[1]
            total_value += fraction * item[0]
            total_weight += fraction * item[1]
            break
        print(f'Iteration  {i} : ({total_value}, {total_weight})')

    return total_value, total_weight

items = [(50, 15), (75, 25), (90, 45)]
capacity = 69

maximum_value = fractional_knapsack(items, capacity)
print('Final Iteration: ', maximum_value)
