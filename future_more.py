import random
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Bayesian network structure
# ---------------------------------------------------------------------------
#
#   GATE_Result --> Outcome
#
# GATE_Result has two states: "Cleared", "Not_Cleared"
# Outcome's *domain itself* depends on the parent state:
#   if GATE_Result = Cleared      -> Outcome in {IIT_Delhi, Not_IIT_Delhi}
#   if GATE_Result = Not_Cleared  -> Outcome in {Got_Job, Got_Married_and_Died}
#
# This avoids the old trick of having 7 separate nodes and manually zeroing
# out "inconsistent" combinations -- here every entry in the joint table is
# a genuinely reachable state, computed directly from real CPT values.

NODES = ["GATE_Result", "Outcome"]

PARENTS = {
    "GATE_Result": [],
    "Outcome": ["GATE_Result"],
}

# Which Outcome values are even possible under each GATE_Result state.
OUTCOME_DOMAIN = {
    "Cleared": ["IIT_Delhi", "Not_IIT_Delhi"],
    "Not_Cleared": ["Got_Job", "Got_Married_and_Died"],
}


def build_random_cpts():
    """Randomly generate the conditional probability tables (CPTs)."""

    p_cleared = random.uniform(0, 0.8)  # P(GATE_Result = Cleared)
    p_iit = random.uniform(0, 1)        # P(Outcome = IIT_Delhi | Cleared)
    p_job = random.uniform(0, 1)        # P(Outcome = Got_Job | Not_Cleared)

    cpts = {
        "GATE_Result": {
            "Cleared": p_cleared,
            "Not_Cleared": 1 - p_cleared,
        },
        "Outcome": {
            "Cleared": {
                "IIT_Delhi": p_iit,
                "Not_IIT_Delhi": 1 - p_iit,
            },
            "Not_Cleared": {
                "Got_Job": p_job,
                "Got_Married_and_Died": 1 - p_job,
            },
        },
    }
    return cpts


def calculate_joint_probabilities(cpts):
    """Multiply out P(GATE_Result) * P(Outcome | GATE_Result) for every
    reachable (gate_result, outcome) pair. No dead branches, no zeroing."""

    joint_probabilities = {}
    for gate_state, p_gate in cpts["GATE_Result"].items():
        for outcome in OUTCOME_DOMAIN[gate_state]:
            p_outcome_given_gate = cpts["Outcome"][gate_state][outcome]
            val = p_gate * p_outcome_given_gate
            joint_probabilities[(gate_state, outcome)] = val
            print(f"P(GATE_Result={gate_state}, Outcome={outcome}) = {val:.4f}")

    return joint_probabilities


def displaying_highest_joint_probability(joint_probabilities):
    max_state = max(joint_probabilities, key=joint_probabilities.get)
    max_probability = joint_probabilities[max_state]

    print("\nMost likely future:")
    for name, value in zip(NODES, max_state):
        print(f"  {name}: {value}")
    print(f"Joint probability of this future: {max_probability:.4f} ({max_probability:.2%})")


def plot_joint_probabilities(joint_probabilities):
    labels = [f"{gate}\n{outcome}" for gate, outcome in joint_probabilities.keys()]
    values = list(joint_probabilities.values())

    plt.figure(figsize=(8, 5))
    plt.bar(range(len(values)), values, tick_label=labels)
    plt.xlabel("State")
    plt.ylabel("Joint Probability")
    plt.title("Joint Probability Distribution of the Bayesian Network")
    plt.tight_layout()
    plt.savefig("visualisation/joint_probability_distribution.png")
    plt.show()


def future():
    cpts = build_random_cpts()
    joint_probabilities = calculate_joint_probabilities(cpts)
    displaying_highest_joint_probability(joint_probabilities)
    return NODES, PARENTS, cpts, joint_probabilities


def main():
    nodes, parents, cpts, joint_probabilities = future()
    print("-" * 60)
    displaying_highest_joint_probability(joint_probabilities)
    plot_joint_probabilities(joint_probabilities)


if __name__ == "__main__":
    main()