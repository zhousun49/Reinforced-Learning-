import numpy as np
import random
from su_action import su_action
import csv
#Initialization of 64*6. Storage type is a dict
actions = ['request_food_type', 'request_price', 'request_location','explicit_confirm_food_type', 'explicit_confirm_price', 'explicit_confirm_location']
initialization = {}
for rep in range(64):
    arr = []
    for i in actions:
        one_step = {}
        one_step["Q_val"] = 0
        one_step['action'] = i 
        arr.append(one_step)
    initialization[rep] = arr
# print(initialization)

#Initialize all other variables
gamma = 0.99
with open("rewards.csv", 'w') as rewards_file:  
    writer = csv.writer(rewards_file) 
    for i in range(5000):
        alpha = 1/(1+i)
        state = [0]*len(actions)
        total_reward = 0
        last_iter = []
        #Implementation of timeout: no more than 30 episodes
        for j in range(50):
            #Greedy Approach: 0.8/0.2
            #Only exploit at the last iteration
            if (random.random() < 0.8) or (i == 4999):
                current_state = np.packbits(state, bitorder="little")[0]
                maxQval = max(initialization[current_state], key=lambda x:x['Q_val'])
                action = maxQval['action']
                action_id = actions.index(action)
            else: 
                action = random.choice(actions)
                action_id = actions.index(action)
            # print("state: ", state)
            # print("action: ", action)
            SU_action = su_action(action)
            lst = [str(x) for x in state]
            lst.append(action.upper())  
            last_iter.append(lst)
            # print("SU action: ", SU_action)
            if ("confirm" in action):
                #The way I initialized the actions list, check index - 3
                #If a state is confirmed before filled, continue to the next iteration 
                # print("action: ", action)
                # print("action id: ", action_id)
                # print(actions[action_id - 3])
                if (state[action_id - 3] == 0):
                    # print("Above holds true")
                    total_reward -= 5
                    reward = -5
                    prev_state = np.packbits(state, bitorder="little")[0]
                    prev_state_action = next(item for item in initialization[prev_state] if item["action"] == action)
                    prev_state_action["Q_val"] = prev_state_action['Q_val'] + alpha*(reward + gamma*prev_state_action['Q_val'] - prev_state_action['Q_val'])
                    continue
                #Negative action, set the previous filled slot to 0, continue to the next iteration
                if ("neg" in SU_action):
                    # print("!!! Negative Action")
                    total_reward -= 5
                    reward = -5
                    prev_state = np.packbits(state, bitorder="little")[0]
                    state[action_id - 3] = 0
                    new_state = np.packbits(state, bitorder="little")[0]
                    prev_state_action = next(item for item in initialization[prev_state] if item["action"] == action)
                    maxQval = max(initialization[new_state], key=lambda x:x['Q_val'])
                    prev_state_action["Q_val"] = prev_state_action['Q_val'] + alpha*(reward + gamma*maxQval['Q_val'] - prev_state_action['Q_val'])
                    continue
            #Continue to the next iteration if the simulated user action is irrelevant. 
            if (SU_action == "irrelevant"):
                total_reward -= 5
                reward = -5
                prev_state = np.packbits(state, bitorder="little")[0]
                prev_state_action = next(item for item in initialization[prev_state] if item["action"] == action)
                prev_state_action["Q_val"] = prev_state_action['Q_val'] + alpha*(reward + gamma*prev_state_action['Q_val'] - prev_state_action['Q_val'])
                continue
            prev_state = np.packbits(state, bitorder="little")[0]
            # print("state: ", state)
            state[action_id] = 1
            new_state = np.packbits(state, bitorder="little")[0]
            prev_state_action = next(item for item in initialization[prev_state] if item["action"] == action)
            maxQval = max(initialization[new_state], key=lambda x:x['Q_val'])
            if state == [1]*6: 
                reward = 500-5
                total_reward += 500
                prev_state_action["Q_val"] = prev_state_action['Q_val'] + alpha*(reward + gamma*maxQval['Q_val'] - prev_state_action['Q_val'])
                break
            else: 
                reward = -5
                total_reward -= 5
                prev_state_action["Q_val"] = prev_state_action['Q_val'] + alpha*(reward + gamma*maxQval['Q_val'] - prev_state_action['Q_val'])
        #Only writing the last iteration
        if i == 4999: 
            with open("policy.csv", 'w') as output_file:  
                opwriter = csv.writer(output_file)
                fields = ['FOOD_TYPE_FILLED', 'PRICE_FILLED', 'LOCATION_FILLED', 'FOOD_TYPE_CONF', 'PRICE_CONF', 'LOCATION_CONF', 'BEST_ACTION']
                opwriter.writerows([fields])
                opwriter.writerows(last_iter)
        # print('Current Episode Number: ', i + 1, ' has a reward of ', total_reward)  
        # writing data rows  
        writer.writerows([[str(i+1), str(total_reward)]])  







