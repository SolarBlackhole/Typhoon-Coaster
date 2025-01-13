import time
import threading

estop = False
simulation = True

def simulate_launch_1train():
    global simulation
    global estop
    print("Simulating Launch Coaster with 1 train")
    print("Train 1 will start in the station")
    blocks = [1, 0, 0, 0]
    block_names = ["Station", "Launch", "Midcourse Brake", "Final Brake"]
    simulation = True
    while(simulation):
        if not estop:
            print("Input 'go' to dispatch the train, or 'exit' to end the simulation")
            print("Incase of an emergency, input 'estop' to stop all trains")
            dispatch = input()
        else:
            print("Input 'reset' to reset the emergency stop, or 'exit' to end the simulation")
            dispatch = input()
        if dispatch == "go" and not estop:
            if blocks[0] == 1:
                print("Dispatching Train 1")
                train1 = threading.Thread(target=train_course, args=(1, blocks, 0, block_names))
                train1.start()
            else:
                print('No trains in the station')
        elif dispatch == "estop":
            print("Emergency Stop Activated. Train Stopped at Current Block")
            estop = True
        elif dispatch == "reset" and estop:
            print("Resetting Emergency Stop, Train will continue")
            estop = False
        elif dispatch == "exit":
            simulation = False
        else:
            print("Invalid Input")
            pass

def train_course(train_num, blocks, current_block, block_names):
    global estop
    global simulation
    while True:
        if estop:
            print(f"Train {train_num} is stopped at {block_names[current_block]}")
            time.sleep(10)
            continue

        dispatched, current_block = advance_train(train_num, blocks, current_block, block_names)
        if current_block == 1:
            print(f"Train {train_num}: Preparing for Launch, Checking for possible Estop and clear midcourse brake")
            
        time.sleep(5)
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

def next_block_occuppied(blocks, next_block):
    return blocks[next_block] != 0