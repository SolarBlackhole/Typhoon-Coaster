import time
import threading

def simulate_lift_1train():
    print("Simulating Lift Hill Coaster with 1 train")
    print("Train 1 will start in the station")
    blocks = [True, False, False, False]
    # Station, Lift Hill, Midcourse Brake, Final Brake
    simulation = True
    while(simulation):
        print("Train 1 is in the station")
        print("Input 'go' to dispatch the train, or 'exit' to end the simulation")
        dispatch = input()
        if dispatch == "go":
            blocks[0] = False
            blocks[1] = True
            print("Train 1 is on the lift hill")
            time.sleep(5) # Simulating the time it takes for the train to reach the end of the block
            blocks[1] = False
            blocks[2] = True
            print("Train 1 is on the midcourse brake")
            time.sleep(5)
            blocks[2] = False
            blocks[3] = True
            print("Train 1 is on the final brake")
            time.sleep(5)
            blocks[3] = False
            blocks[0] = True
            print("Train 1 is back in the station")
        elif dispatch == "exit":
            simulation = False
        else:
            print("Invalid Input")
            pass
        
def simulate_lift_2trains():
    print("Simulating Lift Hill Coaster with 2 trains")
    print("Train 1 will start in the station")
    print("Train 2 will start on the final brake")
    blocks = [1, 0, 0, 2]
    block_names = ["Station", "Lift Hill", "Midcourse Brake", "Final Brake"]
    # Station, Lift Hill, Midcourse Brake, Final Brake
    simulation = True
    current_block_1 = 0
    current_block_2 = 3
    while(simulation):
        print("Train 1 is in the station")
        print("Train 2 is on the final brake")
        print("Input 'go' to dispatch a train, or 'exit' to end the simulation")
        dispatch = input()
        if dispatch == "go":
            # TODO: Implement a way to dispatch the trains
            pass

            
# def train_1_tracker(blocks):
#     while(blocks[0] == True):
#         print("Train 1 is in the station")
#         time.sleep(1)
#     while(blocks[1] == True):
#         print("Train 1 is on the lift hill")
#         time.sleep(1)
#     while(blocks[2] == True):
#         print("Train 1 is on the midcourse brake")
#         time.sleep(1)
#     while(blocks[3] == True):
#         print("Train 1 is on the final brake")
#         time.sleep(1)

# def train_2_tracker(blocks):
#     while(blocks[0] == 2):
#         print("Train 2 is in the station")
#         time.sleep(1)
#     while(blocks[1] == 2):
#         print("Train 2 is on the lift hill")
#         time.sleep(1)
#     while(blocks[2] == 2):
#         print("Train 2 is on the midcourse brake")
#         time.sleep(1)
#     while(blocks[3] == 2):
#         print("Train 2 is on the final brake")
#         time.sleep(1)

def advance_train_1(blocks, current_block, block_names):
    next_block = (current_block + 1) % 4
    if next_block_occupied(blocks, current_block) == False:
        print("Train 1: " + block_names[current_block] + " -> " + block_names[next_block])
        blocks[current_block] = False
        blocks[next_block] = True
        return True, next_block
    else:
        print("Train 1: " + block_names[current_block] + " -> " + block_names[current_block] + " (Waiting)")
        return False, current_block
    
def advance_train_2(blocks, current_block, block_names):
    next_block = (current_block + 1) % 4
    if next_block_occupied == False:
        print("Train 2: " + block_names[current_block] + " -> " + block_names[next_block])
        blocks[current_block] = False
        blocks[next_block] = 2
        return True, next_block
    else:
        print("Train 2: " + block_names[current_block] + " -> " + block_names[current_block] + " (Waiting)")
        return False, current_block
    
    
def next_block_occupied(blocks, current_block):
    next_block = (current_block + 1) % 4
    if blocks[next_block] == True or blocks[next_block] == 2:
        return True
    else:
        return False