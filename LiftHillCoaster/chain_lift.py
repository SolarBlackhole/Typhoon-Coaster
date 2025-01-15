import random

class Chain_Lift:
    chain_lift = False
    chain_lift_speeds = [0, 5, 10]
    current_speed = chain_lift_speeds[0]

    def start_chain_lift(self, train_num):
        broken_chain = random.randint(0, 10)
        if broken_chain == 1:
            print("Chain Lift is broken, No Trains can enter the lift hill")
            return False
        else:
            chain_lift = True
            print("Chain Lift Started for Train " + str(train_num))
            self.set_chain_lift_speed(10)
            return True

    def stop_chain_lift(self):
        global chain_lift
        global current_speed
        current_speed = self.chain_lift_speeds[0]
        chain_lift = False

    def set_chain_lift_speed(self, speed):
        global current_speed
        if not speed in self.chain_lift_speeds:
            print("Invalid Speed")
            return
        if chain_lift:
            current_speed = speed
            print("Chain Lift: Speed set to " + str(speed) + " mph")
        else:
            print("Chain Lift: is not running")



