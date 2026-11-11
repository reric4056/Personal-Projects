class Mission:
    def __init__(self, mission_name, location, objective):
        self.mission_name = mission_name
        self.location = location
        self.objective = objective
        self.difficulty = "Unknown"
        self.completed = False
        self.assigned_agent = None

    def __repr__(self):
        return f"Mission(mission_name={self.mission_name}, location={self.location}, objective={self.objective})"

    def briefing(self):
        print(f"Mission Briefing: ")
        print(f"{self.mission_name}")
        print(f"Location: {self.location}")
        print(f"Objective: {self.objective}")
        print(f"Difficulty: {self.difficulty}")

        if self.assigned_agent is not None:
            print(f"Assigned Agent: {self.assigned_agent.codename}")
        else:
            print("No agent assigned yet.")

    def change_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty
        print(f"Mission {self.mission_name} difficulty changed to: {self.difficulty}")

    def complete_mission(self, agent):
        if self.completed:
            print(f"Mission {self.mission_name} has already been completed.")

        elif self.assigned_agent is agent:
            self.completed = True
            agent.current_mission = None
            self.assigned_agent = None
            print(f"Mission {self.mission_name} has been completed.")
        else:
            print(f"Agent {agent.codename} is not assigned to this mission.")

