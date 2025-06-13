from typing import List

def max_score(tokens: List[int], power: int) -> int:
    tokens.sort()
    left, right = 0, len(tokens) - 1
    score = max_score = 0

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score, score)
        elif score >= 1:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return max_score

if __name__ == "__main__":
    tokens = list(map(int, input("Enter values: ").strip().split()))
    power = int(input("Enter power: ").strip())
    print(max_score(tokens, power))
