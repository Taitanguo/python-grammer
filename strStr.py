source, target = [raw_input() for _ in range(2)]
score = 0
for i in range(len(source)):
	if source[i : i + len(target)] == target:
		score += 1
print score