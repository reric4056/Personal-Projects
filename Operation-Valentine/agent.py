class Agent:
    def __init__(self, name, codename, clearance_level):
        self.name = name
        self.codename = codename
        self.clearance_level = clearance_level
        self.money = 1000
        self.is_disguised = True
        self.current_mission = None

    def __repr__(self):
        return f"Agent(name={self.name}, codename={self.codename}, clearance_level={self.clearance_level})"

    def introduce(self):
        print(f"Agent {self.codename}: {self.name}")
        print(f"Clearance Level: {self.clearance_level}")
        print(f"Available Funds: ${self.money}")

    def place_bet(self, amount):
        if amount <= 0:
            print("Invalid wager.")
        elif amount > self.money:
            print("Insufficient funds for this wager.")
        else:
            self.money -= amount
            print(f"Placed a bet of ${amount}. Remaining funds: ${self.money}")

    def change_disguise(self):
        self.is_disguised = not self.is_disguised
        disguise_status = "disguised" if self.is_disguised else "not disguised"
        print(f"Agent {self.codename} is now {disguise_status}.")

    def accept_mission(self, mission):
        if self.current_mission is not None:
            print("You are already on a mission. Complete it before accepting a new one.")
        elif mission.completed:
            print("This mission has already been completed.")
        elif mission.assigned_agent is not None:
            print("This mission is already assigned to another agent.")
        else:
            self.current_mission = mission
            mission.assigned_agent = self
            print(f"Agent {self.codename} has accepted the mission: {mission.mission_name}")

    def report_status(self):
        disguise_status = "disguised" if self.is_disguised else "not disguised"
        mission_status = self.current_mission.mission_name if self.current_mission else "No active mission"
        print(f"Agent {self.codename} Status Report:")
        print(f"Disguise Status: {disguise_status}")
        print(f"Current Mission: {mission_status}")
        print(f"Available Funds: ${self.money}")