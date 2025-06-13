def find_ranks(score):
    sorted_scores = sorted(score, reverse=True)
    rank_map = {}
    for i, val in enumerate(sorted_scores):
        if i == 0:
            rank_map[val] = "Gold Medal"
        elif i == 1:
            rank_map[val] = "Silver Medal"
        elif i == 2:
            rank_map[val] = "Bronze Medal"
        else:
            rank_map[val] = str(i + 1)
    result = [rank_map[s] for s in score]
    return result

if __name__ == "__main__":
    score = list(map(int, input("Enter scores separated by space: ").strip().split()))
    print(find_ranks(score))
