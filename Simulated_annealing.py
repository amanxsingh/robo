import math
import random
import matplotlib.pyplot as plt
 
#Solving a cubic equation using simulated annealing.
def simulated_Annealing(s0, T_max, T_min, alpha):
    current_state= s0
    T = T_max
    E = []
    states=[]
    states.append(s0)
    E.append(Energy(s0))

    while T>T_min:

        #Generate a random neighbour
        next_state = getRandomNeighbour(current_state)

        #Calculate the change in Energy 
        delta_E = Energy(next_state) - Energy(current_state)

        #Decision rule
        if delta_E < 0:
            current_state = next_state
            states.append(current_state)
            E.append(Energy(current_state))

        else:
            r = random.random()

            if r < pow(math.e, -delta_E/T):
                current_state = next_state
                states.append(current_state)
                E.append(Energy(current_state))
        T = T*alpha
    plt.plot(states, E, label="Simulated Annealing Plot")
    plt.plot(states[-1], E[-1], color='red', marker='o', label="Final Solution and Energy")
    plt.text(states[-1], 0.5+E[-1], f"({states[-1]:.2f}, {E[-1]:.2f})")
    plt.plot(states[E.index(min(E))], min(E), color='green', marker='o', label='Best Solution of the Run')
    plt.text(states[E.index(min(E))],  0.5+min(E),f"({states[E.index(min(E))]:.2f},{min(E):.2f})")
    plt.gcf().text(0.5, 0.01, f"The Final Solution state: {states[-1]:.2f} and Energy: {E[-1]:.2f}",
               ha='center', fontsize=12)
    plt.xlabel("States")
    plt.ylabel("Energy")
    plt.title("Simulated Annealing of x3-10x-2x2+10")
    plt.legend()
    plt.show()
    return current_state

def getRandomNeighbour(currentState):
    return random.uniform(-3,3)

def Energy(state):
    return (state**3)-(10.0*state)-(2.0*(state**2))+10.0

print("******Welcome to simulated Annealing of x3-10x-2x2+10******")
Initial_State = float(input("What is the initial State:"))
Initial_Temparature = float(input("What is the initial Temparature:"))
Threshold_Temparature = float(input("What is the Threshold Temparature:"))
Cooling_Rate = float(input("What is the Cooling Rate:"))

Solution = simulated_Annealing(Initial_State, Initial_Temparature, Threshold_Temparature, Cooling_Rate)
