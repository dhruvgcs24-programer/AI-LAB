class VacuumCleanerAgent:

    def __init__(self):
      
        self.model = {
            "A": "Unknown",
            "B": "Unknown",
            "path1": "Unknown",
            "path2": "Unknown"
        }

        self.position = "A"

    def perceive(self, environment):

      
        self.model[self.position] = environment[self.position]

  
        self.model["path1"] = environment["path1"]
        self.model["path2"] = environment["path2"]

    def choose_action(self):

        
        if self.model[self.position] == "Dirty":
            return "Suck"

      
        if self.position == "A":

           
            if self.model["path1"] == "Clear":
                return "Move to B using Path 1"

           
            elif self.model["path2"] == "Clear":
                return "Move to B using Path 2"

            # Both paths blocked
            else:
                return "No path available"

        
        elif self.position == "B":

            if self.model["path1"] == "Clear":
                return "Move to A using Path 1"

            elif self.model["path2"] == "Clear":
                return "Move to A using Path 2"

            else:
                return "No path available"

    def execute(self, action):

        if action == "Suck":
            print("Cleaning Room", self.position)
            self.model[self.position] = "Clean"

        elif "Move to B" in action:
            print(action)
            self.position = "B"

        elif "Move to A" in action:
            print(action)
            self.position = "A"

        elif action == "No path available":
            print("Both paths are blocked!")




environment = {
    "A": "Clean",
    "B": "Dirty",  
    "path1": "Blocked",
    "path2": "Clear"
}



agent = VacuumCleanerAgent()


for i in range(5):

    print("\nCurrent Room:", agent.position)

  
    agent.perceive(environment)

 
    action = agent.choose_action()

    print("Action:", action)

  
    agent.execute(action)

  
    if action == "Suck":
        environment[agent.position] = "Clean"

  
    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("\nBoth rooms are clean!")
        break
