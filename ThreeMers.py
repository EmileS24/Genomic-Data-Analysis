# Import the necessary libraries
import matplotlib.pyplot as plt
from collections import Counter

# Read the bacterial genome sequence from a file
with open('genomicDataset.fna', 'r') as f:
    f.readline() # Skip the first line
    for line in f:
      if not line.startswith(">"):
        genome = f.read().replace('N', '') # Remove the N's

# Generate all 3-mers and count their occurrences
kmers = [genome[i:i+3] for i in range(len(genome)-2)]
counts = Counter(kmers)
sorted_dict = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
top_20 = dict(list(sorted_dict.items())[:20])

# Generate a histogram of the counts
plt.bar(top_20.keys(), top_20.values())
plt.xlabel('3-mers')
plt.ylabel('Count')
plt.title('Histogram of 3-mers in Bacterial Genome')
plt.show()