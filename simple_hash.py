import sys
from collections import Counter
from pyfasta import Fasta

# build sketches from the 100 lowest 15 mers

def get_sketch(fasta, n_kmers=100, k=15):
    # use a sample of kmers from a fastq
    hash_count = Counter()
    f = Fasta(fasta)
    for chrom in f.keys():
         seq = f[chrom]
         for i in range(len(seq)-k):
               kmer = seq[i:i+k]
               hash_count[kmer] += 1
    
    hashes_used = 0
    hashed_sketch = []
    for kmer in sorted(hash_count.keys()):
         if hashes_used <= n_kmers:
               #print(hash_count[i])
               hashed_sketch.append(kmer)
               hashes_used += 1

    return hashed_sketch
