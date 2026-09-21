import random
import time

class VacuumEnvironment:
    def __init__(self):
        self.locations = ['A', 'B']
        self.status = {
            'A': random.choice(['Clean', 'Dirty']),
            'B': random.choice(['Clean', 'Dirty'])
        }
        self.agent_location = random.choice(self.locations)
        self.performance_score = 0

    def get_percept(self):
        """Returns the current location and its status."""
        return self.agent_location, self.status[self.agent_location]

    def execute_action(self, action):
        """Applies the agent's action to the environment."""
        print(f"Action taken: {action}")
        
        if action == 'Suck':
            self.status[self.agent_location] = 'Clean'
            self.performance_score += 10  
        elif action == 'MoveRight':
            self.agent_location = 'B'
            self.performance_score -= 1  
        elif action == 'MoveLeft':
            self.agent_location = 'A'
            self.performance_score -= 1  

    def display_state(self):
        """Prints the current state of the environment."""
        print(f"\n--- Environment State ---")
        print(f"Room A: {self.status['A']} | Room B: {self.status['B']}")
        print(f"Vacuum Position: Room {self.agent_location}")
        print(f"Current Performance Score: {self.performance_score}")
        print("-------------------------")


class SimpleReflexAgent:
    def program(self, percept):
        """Determines the next action based strictly on the current percept."""
        location, status = percept
        
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'MoveRight'
        elif location == 'B':
            return 'MoveLeft'


# --- Simulation Run ---
if __name__ == "__main__":
    env = VacuumEnvironment()
    agent = SimpleReflexAgent()
    
    print("Initial Environment Setup:")
    env.display_state()
    time.sleep(1)

    for step in range(1, 5):
        print(f"\n=== Step {step} ===")
        
        percept = env.get_percept()
        print(f"Agent perceives: Location {percept[0]} is {percept[1]}")
        
        action = agent.program(percept)
        
        env.execute_action(action)
        env.display_state()
        
        time.sleep(1)
        
        if env.status['A'] == 'Clean' and env.status['B'] == 'Clean' and action == 'Suck':
            print("\nBoth rooms are now clean! Simulation ending.")
            break
