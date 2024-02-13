
heads_count = 0
tails_count = 0

# Simulate 100 coin flips
for _ in range(100):
    flip_result = random.choice(['Heads', 'Tails'])
    if flip_result == 'Heads':
        heads_count += 1
    else:
        tails_count += 1
