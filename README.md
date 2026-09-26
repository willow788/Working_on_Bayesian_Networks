# Working on Bayesian Networks

A small Python project for learning and experimenting with **Bayesian networks**, conditional probability tables (CPTs), joint probability distributions, and simple visualisations.

The examples build networks manually, assign randomly generated probabilities, calculate the probability of each reachable state, identify the most likely outcome, and display results with Matplotlib.

## Repository contents

```text
.
├── Networks in here!/
│   ├── simple_BN.py
│   ├── a_little_more_complex_BN.py
│   └── future_more.py
├── visualisation/
│   └── joint_probability_distribution.png
└── LICENSE
```

### Examples

- **`simple_BN.py`**
  - Builds a two-node rain and wet-grass network.
  - Builds a three-node `Meet → Talk → FallInLove` network.
  - Prints joint probabilities and saves a bar chart to `visualisation/joint_probability_distribution.png`.

- **`a_little_more_complex_BN.py`**
  - Demonstrates a larger network based on GATE results and possible future outcomes.
  - Generates a joint probability distribution and reports the most likely state.
  - Displays the distribution using Matplotlib.

- **`future_more.py`**
  - Provides a simplified, cleaner version of the GATE-result network.
  - Restricts outcomes to reachable branches such as `IIT_Delhi`, `Not_IIT_Delhi`, `Got_Job`, and `Got_Married_and_Died`.
  - Prints probabilities, identifies the most likely future, and plots the results.

## Requirements

- Python 3.8 or later
- Matplotlib

The standard-library `random` module is used to generate example probabilities. No external Bayesian-network library is required.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/willow788/Working_on_Bayesian_Networks.git
   cd Working_on_Bayesian_Networks
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependency:

   ```bash
   python -m pip install matplotlib
   ```

## Running the examples

From the repository root, run any example as a Python script:

```bash
python "Networks in here!/simple_BN.py"
python "Networks in here!/a_little_more_complex_BN.py"
python "Networks in here!/future_more.py"
```

The scripts print the generated conditional probabilities and joint probability distributions to the terminal. Depending on the example, a Matplotlib window opens and/or a chart is saved in the `visualisation/` directory.

## How the calculations work

For a Bayesian network, the joint probability of a complete assignment is calculated by multiplying the relevant conditional probabilities. For example, the rain and wet-grass example uses:

```text
P(Rain, WetGrass) = P(Rain) × P(WetGrass | Rain)
```

The larger examples apply the same idea across multiple nodes and only include valid combinations of parent and child states.

## Reproducibility

The examples currently generate probabilities with `random.uniform()`, so the output changes each time they run. To reproduce a particular result, set a random seed before generating the CPTs, for example:

```python
import random

random.seed(42)
```

## Notes

This repository is intended as an educational project and a workspace for experimenting with Bayesian-network concepts. The probabilities are randomly generated demonstration values rather than estimates learned from a dataset.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.
