# sort_cards.py

def sort_cards():
    list_input = list(map(int, input("Enter cards (space-separated): ").strip().split()))
    print("Sorted cards:", sorted(list_input))

if __name__ == "__main__":
    sort_cards()
