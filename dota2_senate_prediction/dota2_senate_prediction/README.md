# Dota2 Senate Prediction

This Python script predicts the winning party in the Dota2 senate simulation. The input is a string consisting of characters `R` (Radiant) and `D` (Dire). Senators take turns banning each other in the order they appear, and the process continues in rounds until one party remains.

## How it Works
- Use two queues to track indices of `R` and `D`.
- In each round, compare the front senators.
- The earlier senator bans the other and goes to the next round by re-appending their index with `n`.

## Usage
Run the script and input a senate string (e.g., `RDD`).

## Test Cases
See `test_cases.txt` for sample inputs and expected outputs.
