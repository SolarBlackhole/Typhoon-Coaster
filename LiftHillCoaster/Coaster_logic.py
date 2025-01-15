import time
import threading
import chain_lift

estop = False
simulation = True
fault = False

def simulate_lift_1train():
    global simulation
    global estop
    global fault
    print("Simulating Lift Hill Coaster with 1 train")
    print("Train 1 will start in the station")
    blocks = [1, 0, 0, 0]
    block_names = ["Station", "Lift Hill", "Midcourse Brake", "Final Brake"]
    simulation = True
    while(simulation):
        if not estop:
            print("Input 'go' to dispatch the train, or 'exit' to end the simulation")
            print("Incase of an emergency, input 'estop' to stop all trains")
            command = input()
        elif estop and not fault:
            print("Input 'reset' to reset the emergency stop, or 'exit' to end the simulation")
            command = input()
        elif fault:
            print("Input 'repair' to repair the chain lift, or 'exit' to end the simulation")
            command = input()
        if command == "go" and not estop:
            if blocks[0] == 1:
                print("Dispatching Train 1")
                train1 = threading.Thread(target=train_course, args=(1, blocks, 0, block_names))
                train1.start()
            else:
                print('No trains in the station')
        elif command == "estop":
            print("Emergency Stop Activated. Train Stopped at Current Block")
            estop = True
        elif command == "reset" and estop:
            print("Resetting Emergency Stop, Train will continue")
            estop = False
        elif command == "exit":
            simulation = False
        else:
            print("Invalid Input")
            pass
        
def simulate_lift_2trains():
    global estop
    global simulation
    global fault
    print("Simulating Lift Hill Coaster with 2 trains")
    print("Train 1 will start in the station")
    print("Train 2 will start on the final brake")
    blocks = [1, 0, 0, 2]
    block_names = ["Station", "Lift Hill", "Midcourse Brake", "Final Brake"]
    # Station, Lift Hill, Midcourse Brake, Final Brake
    simulation = True
    current_block_1 = 0
    current_block_2 = 3
    train1 = threading.Thread()
    train2 = threading.Thread()
    while(simulation):
        if not estop and not fault:
            print("Input 'go' to dispatch a train, 'enter' to bring in train 2 to the station or 'exit' to end the simulation")
            print("Incase of an emergency, input 'estop' to stop all trains")
            dispatch = input()
        elif estop and not fault:
            print("Input 'reset' to reset the emergency stop, or 'exit' to end the simulation")
            dispatch = input()
        elif fault:
            print("Input 'repair' to repair the chain lift, or 'exit' to end the simulation")
            dispatch = input()
        if dispatch == "go" and not estop:
            if blocks[0] == 1:
                print("Dispatching Train 1")
                train1 = threading.Thread(target=train_course, args=(1, blocks, current_block_1, block_names))
                train1.start()
            elif blocks[0] == 2:
                print("Dispatching Train 2")
                train2 = threading.Thread(target=train_course, args=(2, blocks, current_block_2, block_names))
                train2.start()
            else:
                print('No trains in the station')
        elif dispatch == "enter" and not estop:
            if blocks[3] == 2 and blocks[0] == 0:
                print("Bringing Train 2 to the station")
                blocks[3] = 0
                blocks[0] = 2
                current_block_2 = 0
            else:
                print("Train 2 is not in the final brake or there is a train in the station")
        elif dispatch == "estop":
            print("Emergency Stop Activated. All Trains Stopped at Current Blocks")
            estop = True
        elif dispatch == "reset" and estop:
            print("Resetting Emergency Stop, Trains will continue")
            estop = False
        elif dispatch == "exit":
            simulation = False
            train1.join()
            train2.join()

# Cycle the train through the course until it reaches the station

def train_course(train_num, blocks, current_block, block_names):
    global estop
    global simulation
    global fault
    while True:
        if estop:
            print(f"Train {train_num} is stopped at {block_names[current_block]}")
            time.sleep(10)
            continue

        dispatched, current_block = advance_train(train_num, blocks, current_block, block_names)
        if dispatched:
            chain_lift.start_chain_lift(train_num)
            if not chain_lift.chain_lift:
                fault = True
            time.sleep(2.5)
            if next_block_occuppied(blocks, current_block):
                print("Slowing down lift hill")
                chain_lift.set_chain_lift_speed(5)
        else:
            print(f"Train {train_num}: Failed to dispatch.")
        time.sleep(5)

        if fault:
            print("Fault: Chain Lift is broken")
            print(f"Train {train_num} is stopped at {block_names[current_block]}")
            time.sleep(10)
            continue

        while current_block != 0:
            if estop:
                print(f"Train {train_num} is stopped at {block_names[current_block]}")
                time.sleep(10)
                continue
            if not simulation:
                break
            # print(f"Train {train_num}: {block_names[current_block]}")
            dispatched, current_block = advance_train(train_num, blocks, current_block, block_names)
            if dispatched:
                time.sleep(5)
                # dispatched, current_block = advance_train(train_num, blocks, current_block, block_names)
            else:
                print(f"Train {train_num} is waiting in {block_names[current_block]}")
                # print(f"Train {train_num}: Current Blocks: {blocks}")
                time.sleep(5)
        if current_block == 0:
            break

# Move the train to the next block if it is not occupied

def advance_train(train_num, blocks, current_block, block_names):
    next_block = (current_block + 1) % 4
    if not next_block_occuppied(blocks, next_block) or (current_block == 3 and blocks[0] == 0):
        print(f"Train {train_num}: {block_names[current_block]} -> {block_names[next_block]}")
        blocks[current_block] = 0
        blocks[next_block] = train_num
        return True, next_block
    else:
        print(f"Train {train_num}: {block_names[current_block]} -> {block_names[current_block]} (Waiting)")
        return False, current_block
    
# Check if the next block is occupied

def next_block_occuppied(blocks, next_block):
    return blocks[next_block] != 0