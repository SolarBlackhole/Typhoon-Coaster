from lift_hill import simulate_lift_1train, simulate_lift_2trains

# Lift Hill Block Zones: Station, Lift Hill, Midcourse Brake, Final Brake 
# Launch Block Zones: Station, Launch, Midcourse Brake, Final Brake
# The blocks are used to determine the current block a train is in
# In the case of a launch coaster, a train can not be in the launch block and midcourse brake block at the same time, so the blocks are exclusive



def lift_hill_coaster():
    print("Lift Hill Coaster Simulation")
    print("Please select the number of trains you would like to simulate")
    print("1. 1 Train")
    print("2. 2 Trains")
    selection = input()
    if selection == "1":
        print("1 Train Selected")
        simulate_lift_1train()
    elif selection == "2":
        print("2 Trains Selected")
        simulate_lift_2trains()
    else:
        print("Invalid Selection")
        pass

def launch_coaster():
    print("Launch Coaster Simulation")
    print("Please select the number of trains you would like to simulate")
    print("1. 1 Train")
    print("2. 2 Trains")
    selection = input()
    if selection == "1":
        print("1 Train Selected")
        pass
    elif selection == "2":
        print("2 Trains Selected")
        pass
    else:
        print("Invalid Selection")
        pass

def main():
    print("Simulating Coaster with 2 trains and 4 blockzones")
    print("Please determine the type of coaster you would like to simulate")
    print("1. Lift Hill Coaster")
    print("2. Launch Coaster")
    selection = input()
    if selection == "1":
        print("Lift Hill Coaster Selected")
        lift_hill_coaster()
    elif selection == "2":
        print("Launch Coaster Selected")
        launch_coaster()
    else:
        print("Invalid Selection")
        main()

if __name__ == '__main__':
    main()