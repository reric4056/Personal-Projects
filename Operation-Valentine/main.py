from agent import Agent
from mission import Mission

def main():
    print("OPERATION VALENTINE")
    print()

    # Create an agent
    name = input("Enter agent's name: ")
    codename = input("Enter agent's codename: ")
    clearance_level = input("Enter agent's clearance level: ")
    agent = Agent(name, codename, clearance_level)

    # Create your first mission
    mission_1 = ""
    location_1 = ""
    objective_1 = ""
    mission_1 = Mission(mission_1, location_1, objective_1)

    # Create your second mission
    mission_2 = ""
    location_2 = ""
    objective_2 = ""
    mission_2 = Mission(mission_2, location_2, objective_2)

    # Create your third mission
    mission_3 = ""
    location_3 = ""
    objective_3 = ""
    mission_3 = Mission(mission_3, location_3, objective_3)

    missions = [mission_1, mission_2, mission_3]

    running = True

    while running:
        print("\n--- Main Menu ---")
        print("1. Introduce Agent")
        print("2. Place a Bet")
        print("3. Change Disguise")
        print("4. Accept a Mission")
        print("5. Report Status")
        print("6. Mission Briefing")
        print("7. Change Mission Difficulty")
        print("8. Complete Mission")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            agent.introduce()
        elif choice == "2":
            amount = float(input("Enter the amount to bet: "))
            agent.place_bet(amount)
        elif choice == "3":
            agent.change_disguise()
        elif choice == "4":
            for i, mission in enumerate(missions):
                print(f"{i + 1}. {mission.mission_name}")
            mission_choice = int(input("Choose a mission to accept: ")) - 1
            if 0 <= mission_choice < len(missions):
                agent.accept_mission(missions[mission_choice])
            else:
                print("Invalid mission choice.")
        elif choice == "5":
            agent.report_status()
        elif choice == "6":
            for i, mission in enumerate(missions):
                print(f"{i + 1}. {mission.mission_name}")
            mission_choice = int(input("Choose a mission for briefing: ")) - 1
            if 0 <= mission_choice < len(missions):
                missions[mission_choice].briefing()
            else:
                print("Invalid mission choice.")
        elif choice == "7":
            for i, mission in enumerate(missions):
                print(f"{i + 1}. {mission.mission_name}")
            mission_choice = int(input("Choose a mission to change difficulty: ")) - 1
            if 0 <= mission_choice < len(missions):
                new_difficulty = input("Enter new difficulty level: ")
                missions[mission_choice].change_difficulty(new_difficulty)
            else:
                print("Invalid mission choice.")
        elif choice == "8":
            if agent.current_mission is not None:
                agent.current_mission.complete_mission(agent)
            else:
                print("No active mission to complete.")
        elif choice == "9":
            running = False
            print("Exiting the program.")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    