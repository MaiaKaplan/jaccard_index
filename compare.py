import sys

from dist import jaccard
from simple_hash import get_sketch

sketch_a = get_sketch(sys.argv[1])
sketch_b = get_sketch(sys.argv[2])

j = jaccard(sketch_a, sketch_b)
print('jaccard index:', j)
# print("sketches", sketch_a, sketch_b)



