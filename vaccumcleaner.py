import random

# ---------- Environment ----------
class Environment:
    def __init__(self):
        # Randomly initialize dirt status of both rooms
        self.status = {
            'A': random.choice(['Dirty', 'Clean']),
            'B': random.choice(['Dirty', 'Clean'])
        }
        self.agent_location = random.choice(['A', 'B'])

    def display(self):
        print(f"Environment: {self.status}  |  Agent at: {self.agent_location}")


# ---------- Simple Reflex Agent ----------
def simple_reflex_agent(env, steps=5):
    print("\n--- SIMPLE REFLEX AGENT ---")
    for step in range(steps):
        location = env.agent_location
        status = env.status[location]
        print(f"\nStep {step+1}:")
        env.display()

        # Reflex rule: if dirty, clean; else move to other room
        if status == 'Dirty':
            print(f"Room {location} is Dirty -> Action: Suck")
            env.status[location] = 'Clean'
        else:
            new_location = 'B' if location == 'A' else 'A'
            print(f"Room {location} is Clean -> Action: Move to {new_location}")
            env.agent_location = new_location


# ---------- Goal-Based Agent ----------
def goal_based_agent(env):
    print("\n--- GOAL-BASED AGENT ---")
    goal_achieved = False
    step = 1

    while not goal_achieved:
        print(f"\nStep {step}:")
        env.display()
        location = env.agent_location
        status = env.status[location]

        if status == 'Dirty':
            print(f"Room {location} is Dirty -> Action: Suck")
            env.status[location] = 'Clean'
        else:
            # Check if goal (both rooms clean) is achieved
            if all(s == 'Clean' for s in env.status.values()):
                goal_achieved = True
                print("Goal achieved: Both rooms are clean!")
                break
            new_location = 'B' if location == 'A' else 'A'
            print(f"Room {location} is Clean -> Action: Move to {new_location}")
            env.agent_location = new_location

        step += 1


if __name__ == "__main__":
    print("===== Simple Reflex Agent Demo =====")
    env1 = Environment()
    simple_reflex_agent(env1)

    print("\n\n===== Goal-Based Agent Demo =====")
    env2 = Environment()
    goal_based_agent(env2)