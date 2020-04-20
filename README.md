# Self Organizing Systems - Assignment 1

Self Organizing Systems - Self Organizing Maps Exercise

## Getting Started

Read through the instructions.pdf

Install SOM Toolbox from [here](http://www.ifs.tuwien.ac.at/dm/somtoolbox/)

[SOM Toolbox Guide](http://www.ifs.tuwien.ac.at/dm/somtoolbox/)

Learn about the dataset at /data/desc.md

### Prerequisites

Have Java Development kit installed.

Note: Under Windows use double backslashes \\\ as path separator.

### Steps

1. Analyze and describe the characteristics
2. Preprocessing
3. SOM Training and Analysis
    1. Train a reasonably sized „regular“ SOM
    2. Analyze different initializations of the SOM
    3. Analyze different map sizes
    4. Analyze different initial neighborhood radius settings
    5. Analyze different initial learning rates
    6. Analyze different scalings
    7. Analyze different max iterations
    8. Detailed analysis of an „Optimal SOM“
4. Summarize your findings

For more information on each step referr to instructions.pdf

# TODO before:

* Check whether we can get the class labels printed on maps (so that we can describe how classes-clusters are related)
* Do some component plane stuff for the dataset explanation thingy

# Stuff to try and compare:

* Hit histogram
    * Also with linear overlay
* Smoothing data histograms (with the corresponding subtypes - e.g. weighted)
	* Play with the number of neighbors that it considers
		* 2, 3, 5, 10, 20, 50, 100
    * Do it only for normal SDH, and if enough time, do for SDH normlized and weighted
* Sky metaphor
  * The normal sky metaphor (where it maps input vectors within the unit),
  and compare it with the same one with pie charts on it.
* Pie charts
* Thematic map
* Quantization errors & mean quantization errors
    * For palette use Palete -> Single Color -> Redscale 32
* Neighborhood Radius
    * use radiuses as: 0.2, 0.4 and 0.6
* Neighborhood knn
    * use k=1, 3 and 10
* P Matrix
* U Matrix
* U+ Matrix
* Metro map
* Minimum Spanning Tree SOM - SMT
* Flow and Borderline-E
* Cluster Connections




## Other

For each of the points in part C of the exercise, do the same visualizations with pre-set parameters.

The decided paramters are:

* 26x26 map size
* 0.75 learn rate
* sigma (neighboring radius) is default val

# Used terms:

* Quantization errors:
	* Average distance between input vectors and their respective „best-matching units“ (Winner)
