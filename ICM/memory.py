class Memory:
    def __init__(self):
        self.values = []
        self.log_probs = []
        self.rewards = []
        self.states = []
        self.new_states = []
        self.actions = []

    def clear_memory(self):
        self.values = []
        self.log_probs = []
        self.rewards = []
        self.actions = []
        self.states = []
        self.new_states = []
    
    def remember(self, state, action, new_state, reward, value, log_prob):
        self.values.append(value)
        self.log_probs.append(log_prob)
        self.rewards.append(reward)
        self.states.append(state)
        self.new_states.append(new_state)
        self.actions.append(action)

    def sample_memory(self):
        return self.states, self.actions, self.new_states,\
                 self.rewards, self.values, self.log_probs
    