# thoughtful.AI

FDE Technical Screen

# Robotic Package Sorter

This repository contains a Python function that classifies packages into the correct stack for a robotic automation system. The sorting rules are as follows:

- A package is **bulky** if:

  - Volume (Width x Height x Length) >= 1,000,000 cm³, or
  - Any single dimension >= 150 cm

- A package is **heavy** if:
  - Mass >= 20 kg

The stacks are:

- **STANDARD**: If a package is neither bulky nor heavy.
- **SPECIAL**: If a package is either bulky or heavy, but not both.
- **REJECTED**: If a package is both bulky and heavy.

Steps:

1. Clone the repository

git clone https://github.com/manish-m-r/thoughtful.AI.git

2. Run the code:

python sorter.py

3. Expected output for sample tests within sorter.py

STANDARD
SPECIAL
SPECIAL
REJECTED
