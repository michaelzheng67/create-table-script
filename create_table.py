import sys
from collections import defaultdict

if len(sys.argv) < 2:
    print("Usage: python create_table.py <argument>")
    sys.exit(1)

headers = sys.argv[1].split(",")

mp = defaultdict(list)
mp_longest_val = {} # header : longest lengthed value (for formatting purposes)

longest_length = 0      # longest lengthed row
num_rows = 0            # number of rows

for h in headers:
    longest_val = len(h) # longest val for this header
    user_input = input(f"Column values for {h}: ")
    vals = user_input.split(",")
    num_rows = max(num_rows, len(vals))

    for v in vals:
        mp[h].append(v)
        longest_val = max(longest_val, len(v))
    
    longest_length += (longest_val + 2) # extra increments for space + '|'
    mp_longest_val[h] = longest_val


# print the header
print("-" * longest_length)
print("|", end="")
for h in headers:
    print(h + ' ' * (mp_longest_val[h] - len(h)) + ' |', end="")
print('') # hacky way to do newline (printing \n gives double newline)
print("-" * longest_length)

# print the values
for i in range(num_rows):
    print("|", end="")
    for h in headers:
        print(mp[h][i] + ' ' * (mp_longest_val[h] - len(mp[h][i])) + ' |', end="")
    print('')
    print("-" * longest_length)