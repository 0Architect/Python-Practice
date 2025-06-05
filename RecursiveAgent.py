class RecursiveAgent:
    def __init__(self, name: str, goal_target: int):
        self.name = name
        self.goal = goal_target
        self.current_state = 0

    def have_attained_goal(self) -> bool:
        if self.current_state == self.goal:
            return True
        return False

    def update_state(self):
        if self.have_attained_goal():
            return
        if self.current_state < self.goal:
            self.current_state += 1
        else:
            self.current_state -= 1
        print(self.current_state)
        self.update_state()

Agent1 = RecursiveAgent("Agent", 10)
print(f"The goal of this is to see if {Agent1.name} can recursively arrive at goal state")
Agent1.update_state()