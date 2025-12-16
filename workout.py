from collections import defaultdict

# Create a defaultdict with int as the default factory
animal_counts = defaultdict(int)

animals = ['dog', 'cat', 'dog', 'dog', 'cat', 'bird']

# Add animals to the dictionary
for animal in animals:
    animal_counts[animal] += 1 # No KeyError, even for the first 'dog' or 'cat'

print(animal_counts)
