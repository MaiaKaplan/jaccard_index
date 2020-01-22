# jaccard_index
A rough measure of similarity between two fasta files

First, the hash is calculated for the input fasta files. 
Secondly, the jaccard is calcualated for the two sketches. 


## Usage example:
```
$ python3 compare.py data/mouse_idh1.txt data/dog_idh1.txt 
jaccard index: 0.01
$ python3 compare.py data/mouse_idh1.txt data/zebrafish_idh1.txt 
jaccard index: 0.01
$ python3 compare.py data/mouse_idh1.txt data/guppy_idh1.txt 
jaccard index: 0.0
$ python3 compare.py data/mouse_idh1.txt data/mouse_idh1.txt
jaccard index: 1.0
```




Note that much of this is based on the 'simplified hashing' slides from a Journal Club at Quinlan Lab
that were posted on twitter Nov 7th, 2019. I was keen on the idea to understand it and wanted to play with 
the code that was posted there to explore toy problems. 

