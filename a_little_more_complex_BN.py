import random
import matplotlib.pyplot as plt


def displaying_highest_joint_probability(joint_probabilities):
    state_names = [
        "GATE",
        "GATE_Cleared",
        "GATE_Not_Cleared",
        "IIT_Delhi",
        "Not_IIT_Delhi",
        "Got_Job",
        "Got_Married_and_Died"
    ]

    possible_states = {
        state: probability
        for state, probability in joint_probabilities.items()
        if probability > 0
    }
    max_state = max(possible_states, key=possible_states.get)
    max_probability = joint_probabilities[max_state]
    print("\nMost likely future:")
    for name, value in zip(state_names, max_state):
        print(f"  {name}: {value}")
    print(f"Joint probability of this future: {max_probability:.4f} ({max_probability:.2%})")

#we will be defining my future using bn
#we will hve 7 nodes : gate, gate_cleared, gate_Not_cleared, after gate clearedd.. got iit_dehli or not_iit_dehli, if not cleared then got a job or got married and died

def future():

    #defining the nodes
    nodes = ['GATE', 'GATE_Cleared', 'GATE_Not_Cleared', 'IIT_Delhi', 'Not_IIT_Delhi', 'Got_Job', 'Got_Married_and_Died']

    #DEFINING THE PARENT CHILD RELATIONSHIPS
    parents = {
        "GATE": [],
        "GATE_Cleared": ["GATE"],
        "GATE_Not_Cleared": ["GATE"],
        "IIT_Delhi": ["GATE_Cleared"],
        "Not_IIT_Delhi": ["GATE_Cleared"],
        "Got_Job": ["GATE_Not_Cleared"],
        "Got_Married_and_Died": ["GATE_Not_Cleared"]
    }

    #defining the conditional probability tables (CPTs)

    #generating a random probability for GATE
    gate_true = random.uniform(0, 0.8)  #probability of clearing GATE

    gate_cleared_true_given_gate = {
        "True": random.uniform(0, 1),
        "False": random.uniform(0, 1)
    }
    iit_delhi_true_given_gate_cleared = {
        "True": random.uniform(0, 1),
        "False": 0.0
    }
    got_job_true_given_gate_not_cleared = {
        "True": random.uniform(0, 1),
        "False": 0.0
    }

    condtional_probabilities = {
        "GATE": {"True": gate_true,
                 "False": 1 - gate_true},
        "GATE_Cleared": {
            gate_state: {"True": probability, "False": 1 - probability}
            for gate_state, probability in gate_cleared_true_given_gate.items()
        },
        "GATE_Not_Cleared": {
            gate_state: {"True": 1 - probability, "False": probability}
            for gate_state, probability in gate_cleared_true_given_gate.items()
        },
        "IIT_Delhi": {
            cleared_state: {"True": probability, "False": 1 - probability}
            for cleared_state, probability in iit_delhi_true_given_gate_cleared.items()
        },
        "Not_IIT_Delhi": {
            cleared_state: {"True": 1 - probability, "False": probability}
            for cleared_state, probability in iit_delhi_true_given_gate_cleared.items()
        },
        "Got_Job": {
            not_cleared_state: (
                {"True": probability, "False": 1 - probability}
                if not_cleared_state == "True"
                else {"True": 0.0, "False": 1.0}
            )
            for not_cleared_state, probability in got_job_true_given_gate_not_cleared.items()
        },
        "Got_Married_and_Died": {
            not_cleared_state: (
                {"True": 1 - probability, "False": probability}
                if not_cleared_state == "True"
                else {"True": 0.0, "False": 1.0}
            )
            for not_cleared_state, probability in got_job_true_given_gate_not_cleared.items()
        }

    }
    #JOINT PROBABILITY DISTRIBUTION
    def calculate_joint_probabilities(conditional_probabilities):
        joint_probabilities = {}
        for gate_state in ["True", "False"]:
            for gate_cleared in ["True", "False"]:
                for gate_not_cleared in ["True", "False"]:
                    for iit_delhi in ["True", "False"]:
                        for not_iit_delhi in ["True", "False"]:
                            for got_job in ["True", "False"]:
                                for got_married_and_died in ["True", "False"]:
                                    if gate_cleared == gate_not_cleared:
                                        val = 0
                                    elif gate_cleared == "False" and (iit_delhi != "False" or
                                                                       not_iit_delhi != "True"):
                                        val = 0
                                    elif gate_cleared == "True" and iit_delhi == not_iit_delhi:
                                        val = 0
                                    elif gate_not_cleared == "False" and (got_job != "False" or
                                                                           got_married_and_died != "False"):
                                        val = 0
                                    elif gate_not_cleared == "True" and got_job == got_married_and_died:
                                        val = 0
                                    else:
                                        val = (
                                            conditional_probabilities["GATE"][gate_state]
                                            * conditional_probabilities["GATE_Cleared"][gate_state][gate_cleared]
                                            * conditional_probabilities["IIT_Delhi"][gate_cleared][iit_delhi]
                                            * conditional_probabilities["Got_Job"][gate_not_cleared][got_job]
                                        )
                                    joint_probabilities[(gate_state, gate_cleared, gate_not_cleared, iit_delhi, not_iit_delhi, got_job, got_married_and_died)] = val
                                    print(f"P(GATE={gate_state}, GATE_Cleared={gate_cleared}, GATE_Not_Cleared={gate_not_cleared}, IIT_Delhi={iit_delhi}, Not_IIT_Delhi={not_iit_delhi}, Got_Job={got_job}, Got_Married_and_Died={got_married_and_died}) = {val:.4f}")
        return joint_probabilities

    def plot_joint_probabilities(joint_probabilities):
        # Extract the joint probabilities and their corresponding states
        states = list(joint_probabilities.keys())
        probabilities = list(joint_probabilities.values())

        # Create a bar plot
        plt.figure(figsize=(12, 6))
        plt.bar(range(len(probabilities)), probabilities, tick_label=[str(state) for state in states])
        plt.xticks(rotation=90)
        plt.xlabel('States')
        plt.ylabel('Joint Probability')
        plt.title('Joint Probability Distribution of the Bayesian Network')
        plt.tight_layout()
        plt.show()

    joint_probabilities = calculate_joint_probabilities(condtional_probabilities)
    displaying_highest_joint_probability(joint_probabilities)
    return nodes, parents, condtional_probabilities, joint_probabilities, plot_joint_probabilities

def main():
    nodes, parents, conditional_probabilities, joint_probabilities, plot_joint_probabilities = future()
    print('--------------------------------------------------------------')

    #displaying the highest joint probability state
    displaying_highest_joint_probability(joint_probabilities)

if __name__ == "__main__":
    main()
    
    



