#we will be generating a very simple Bayesian Network 
#if it rains, the grass will be wet.
import random 
import matplotlib.pyplot as plt


def generating_grass_Wetting_BN():

    #defining the nodes
    nodes = ['Rain', 'WetGrass']

    #specifying the parent-child relationships
    parents = {
        "Rain": [],
        "WetGrass": ["Rain"]

    }

    #defining the conditional probability tables (CPTs)
    #generating a random probability for rain
    rain_true = random.uniform(0.2, 0.8)  #probability of rain
    conditional_probabilities = {
        "Rain": {
            "True": rain_true,
            "False": 1 - rain_true
        },
        "WetGrass": {
            #wet grass cpt will be defined based on the rain node
            #when it rains, the grass is wet with a high probability

            "True": {"True": random.uniform(0.7, 1), #p(WetGrass=True | Rain=True)
                     "False": random.uniform(0, 0.3)}, #p(WetGrass=False | Rain=True)

            #when it doesn't rain, the grass is not wet with a high probability
            "False": {"True": random.uniform(0, 0.3), #p(WetGrass=True | Rain=False)
                      "False": random.uniform(0.7, 1)} #p(WetGrass=False | Rain=False)
        }
    }

    #now computing the joint probability distribution for the network
    joint_probabilities = {}
    for rain_state in ["True", "False"]:

        for wet_grass in ["True", "False"]:

            val = conditional_probabilities["Rain"][rain_state] * conditional_probabilities["WetGrass"][rain_state][wet_grass]

            #make the vals readable by rounding to 4 decimal places
            val = round(val, 4)

            joint_probabilities[(rain_state, wet_grass)] = val

            #printing the joint probabilities for each combination of rain and wet grass states
            print(f"P(Rain={rain_state}, WetGrass={wet_grass}) = {val}")

    return nodes, parents, conditional_probabilities, joint_probabilities


def he_will_fall_in_love_with_me():

    #specifying the nodes
    #we will meet --> will talk --> will fall in love
    #so the nodes are: meet, talk, fall_in_love
    nodes = ['Meet', 'Talk', 'FallInLove'
             ]

    #parents for each node
    parents = {
        "Meet": [],
        "Talk": ["Meet"],
        "FallInLove": ["Talk"]

    }

    #defining the conditional probability tables (CPTs)
    
    will_meet = random.uniform(0, 1) #probability of meeting
    conditional_probabilities = {
        "Meet": {
            "True" : will_meet,
            "False": 1 - will_meet
        },

        #based on the meeting, the probability of talking is defined
        "Talk" : {
            "True" : {"True": random.uniform(0.7, 1), #p(Talk=True | Meet=True)
                     "False": random.uniform(0, 0.3)}, #p(Talk=False | Meet=True)
            "False" : {"True": random.uniform(0, 0.3), #p(Talk=True | Meet=False)
                      "False": random.uniform(0.7, 1)} #p(Talk=False | Meet=False)
        },

        #based on talk and meeting, the probability of falling in love is defined
        "FallInLove": {
            #we have the markov blanket for the node fall in love, which is the talk node
            "True": {"True": random.uniform(0.7, 1), #p(FallInLove=True | Talk=True)
                     "False": random.uniform(0, 0.3)}, #p(FallInLove=False | Talk=True)
            "False": {"True": random.uniform(0, 0.3), #p(FallInLove=True | Talk=False)
                      "False": random.uniform(0.7, 1)} #p(FallInLove=False | Talk=False)
        }
    }

    #now computing the joint probability distribution for the network
    the_bag_of_hope = {}
    for meet_state in ["True", "False"]:
        for talk_state in ["True", "False"]:
            for fall_in_love_state in ["True", "False"]:

                #computing the prob
                prob_val = conditional_probabilities["Meet"][meet_state] * conditional_probabilities["Talk"][meet_state][talk_state] * conditional_probabilities["FallInLove"][talk_state][fall_in_love_state]

                #rounding the prob_val to 4 decimal places
                prob_val = round(prob_val, 4)

                #adding the computed probability to the joint probability distribution
                the_bag_of_hope[(meet_state, talk_state, fall_in_love_state)] = prob_val
    return nodes, parents, conditional_probabilities, the_bag_of_hope

def displaying_the_bag_of_hope(joint_probabilities):
    print('we will display the joint probability distribution for the network in a more readable format')

    for meet_state in ["True", "False"]:
        for talk_state in ["True", "False"]:
            for fall_in_love_state in ["True", "False"]:
                prob_val = joint_probabilities[(meet_state, talk_state, fall_in_love_state)]
                print(f"P(Meet={meet_state}, Talk={talk_state}, FallInLove={fall_in_love_state}) = {prob_val}")

#we will be displaying the joint probability distribution for the network as a graph using matplotlib
def display_graph(joint_probabilities):

    #extracting the keys and values from the joint probability distribution
    key = [", ".join(state) for state in joint_probabilities.keys()]
    values = list(joint_probabilities.values())

    #creating a bar graph to display the joint probability distribution
    plt.bar(range(len(joint_probabilities)), values, tick_label=key)
    plt.xlabel('States (Meet, Talk, FallInLove)')
    plt.ylabel('Probability')
    plt.title('Joint Probability Distribution for the Network')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.savefig('visualisation/joint_probability_distribution.png')


    

       
    


def main():
    nodes, parents, conditional_probabilities, joint_probabilities = generating_grass_Wetting_BN()

    print("Nodes:", nodes)
    print("Parents:", parents)
    print("Conditional Probabilities:", conditional_probabilities)
    print("Joint Probabilities:", joint_probabilities)

    print('--------------****************--------------------------------------')
    new_nodes, new_parents, new_conditional_probabilities, new_joint_probabilities = he_will_fall_in_love_with_me()
    print(f"New Nodes: {new_nodes}")
    print(f"New Parents: {new_parents}")
    print(f"New Conditional Probabilities: {new_conditional_probabilities}")
    print(f"New Joint Probabilities: {new_joint_probabilities}")

    print('--------------****************--------------------------------------')
    displaying_the_bag_of_hope(new_joint_probabilities)
    print('displaying the joint probability distribution for the network as a graph using matplotlib')
    display_graph(new_joint_probabilities)


if __name__ == "__main__":
    main()