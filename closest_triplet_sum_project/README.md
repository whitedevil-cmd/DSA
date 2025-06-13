# Closest Triplet Sum

This Python program finds a triplet in an array whose sum is closest to a given target value.

## How it Works

- Sort the array.
- Use a two-pointer technique to find the closest sum of any three elements.

## Files

- `closest_triplet_sum.py` – Main program.
- `test_closest_triplet_sum.py` – Unit tests using `unittest`.
- `README.md` – Project documentation.

## Example Usage

```bash
$ python closest_triplet_sum.py
Enter number of elements: 6
Enter the array elements: -1 2 1 -4 5 -3
Enter the target sum: 1
Closest triplet sum: 1
```

## Running Tests

```bash
python -m unittest test_closest_triplet_sum.py
```

## License

MIT
