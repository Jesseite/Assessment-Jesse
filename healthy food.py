healthy_food = {"Apple", "Peach"}
available_food = {"Candy", "Chip", "Apple", "Peach"}

true_healthy_food = True

for i in healthy_food:
    if i not in available_food:
        true_healthy_food = False
        break
    
true_healthy_food

print(true_healthy_food)