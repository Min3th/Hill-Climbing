import random

def neighbor_generator(current_pos,change_range,num_neighbors):
    neighbors = []
    while (num_neighbors)>0:
        change_amount = random.uniform(-change_range,change_range)
        new_neighbor = current_pos + change_amount
        neighbors.append(new_neighbor)
        num_neighbors-=1

    return neighbors




def hill_climbing(f,init_sol):
    init_sol = 0
    while True:
        neighbors = neighbor_generator(init_sol)
        best_neighbor = max(neighbors, key =f)
        if f(best_neighbor) <=f(x):
            return x
        x = best_neighbor


def random_restart(no_of_restarts,max_size,min_size):
    set_of_locals = []
    for i in range(no_of_restarts):
        
        init_sol = random.uniform(min_size,max_size)
        local_max = hill_climbing(f,init_sol)
        set_of_locals.append(local_max)
    best_solution = max(set_of_locals)
    return best_solution

print("Welcome to Hill Climbing using Random Restart method")
sol = random_restart()
print("The best solution according to Hill Climbing is : ",sol)

