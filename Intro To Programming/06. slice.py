
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count (2)
print ("number of 2 dollar slices is: ",num_two_dollar_slices)

num_pizzas = len (toppings)
print ("number of pizzas is:", num_pizzas)

print (f"We sell {num_pizzas} different kinds of pizza!")

pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

print ("Our pizzas: ", pizza_and_prices)

pizza_and_prices.sort()
print ("Our pizzas sorted: ",pizza_and_prices)

cheapest_pizza = pizza_and_prices[0][1]
print ("Our cheapest pizza: ", cheapest_pizza)

priciest_pizza = pizza_and_prices [-1][1]
print ("Our most expensive pizza: ", priciest_pizza)

pizza_and_prices.pop()
print ("Slices left: ",pizza_and_prices)

pizza_and_prices.insert(4,[2.5, "peppers"])
print ("Slices now: ", pizza_and_prices)

three_cheapest = pizza_and_prices [:3]
print (f"Our three cheapest pizzas are:  {three_cheapest[0][1]}, {three_cheapest[1][1]}, {three_cheapest[2][1]}")

