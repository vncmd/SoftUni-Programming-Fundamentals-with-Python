population = [int(num) for num in input().split(", ")]
min_wealth = int(input())

if sum(population) / len(population) < min_wealth:
    print("No equal distribution possible")

else:
    for idx in range(len(population)):
        num = population[idx]
        if num < min_wealth:

            result = min_wealth - num
            max_number = max(population)
            max_idx = population.index(max_number)
            check_number = max_number - result
            population[idx] = min_wealth
            population[max_idx] = check_number

    print(population)
