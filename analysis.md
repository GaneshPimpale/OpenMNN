```

 _____                  ______      
|_   _|                 | ___ \     
  | |_ __ _   _ ___ ___ | |_/ /   _ 
  | | '__| | | / __/ __||  __/ | | |
  | | |  | |_| \__ \__ \| |  | |_| |
  \_/_|   \__,_|___/___/\_|   \__, |
                               __/ |
                              |___/ 

TrussPy - Truss Solver for Python
          Version 3.0.1

Dutzler Andreas, Graz University of Technology, 2023
        
```

# Model Summary
Analysis Dimension      "ndim": 3
Number of Nodes       "nnodes": 3
Number of Elements    "nelems": 2
 
System DOF              "ndof": 9
active DOF             "ndof1": 1
locked DOF             "ndof2": 8
 
active DOF          "nproDOF1": [5]
fixed  DOF          "nproDOF0": [0 1 2 3 4 6 7 8]
\pagebreak
 
# Run Simulation

## Summary of Analysis Parameters
|Description                          |Parameter|Value|
|:------------------------------------|:--------|:--|
|Maximum increments                   |   `incs`| 100 |
|Maximum increment recycles           |   `cycl`| 4 |
|Maximum Newton-Rhapson iterations    |   `nfev`| 8 |
|Maximum incremental displacement     |     `du`| 0.02 |
|Maximum incremental LPF              |   `dlpf`| 0.02 |
|Initial control component            |     `j0`| LPF|
|Locked control component             |`j_fixed`| False |
|Maximum incremental overshoot        |  `dxtol`| 1.000001 |
|Tolerance for x                      |   `xtol`| 8 |
|Tolerance for f                      |   `ftol`| 8 |

### Adaptive control for incremental stepwidth
|Description                          |Parameter    |Value|
|:------------------------------------|:------------|:--|
|Adaptive control for inc. stepwidth  |`stepcontrol`| True |
|Minimum step size factor             |     `minfac`| 1e-06 |
|Maximum step size factor             |     `maxfac`| 4 |
|Reduce step size factor              |     `reduce`| 0.125 |
|Increase step size factor            |   `increase`| 0.5 |


## Step 1
* i(1) is index with 1st-biggest component in abs(Dx/Dx,max).
* i(2) is index with 2nd-biggest component in abs(Dx/Dx,max).
* i(3) is index with 3rd-biggest component in abs(Dx/Dx,max).
* i(4) is index with 4th-biggest component in abs(Dx/Dx,max).
* Value(i) is value of i-th component in abs(Dx/Dx,max).
$$\text{Value}_i = \left|\frac{D_x}{D_{x,max}}\right|_i$$

### Increment 1
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.4142135623730954
|  1  |   0  |   2   |4.303e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.6964|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.01393

### Increment 2
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0
|  1  |   0  |  -1   |4.079e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.6705|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.03213

### Increment 3
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0
|  1  |   0  |  -1   |7.852e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.6340|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.05548

### Increment 4
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0
|  1  |   0  |  -1   |1.532e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.5817|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:    0.08456

### Increment 5
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0
|  1  |   0  |  -1   |3.040e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.5055|   0|     nan|
* increase NR-step size by factor:       1.36

* final LPF:     0.1189

### Increment 6
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000002
|  1  |   0  |  -1   |6.131e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.3928|   0|     nan|

* final LPF:      0.155

### Increment 7
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000002
|  1  |   0  |  -1   |5.048e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.2609|   0|     nan|

* final LPF:     0.1759

### Increment 8
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000002
|  1  |   0  |  -1   |5.338e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.1297|   0|     nan|

* final LPF:     0.1863

### Increment 9
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999994
|  1  |   0  |  -1   |5.483e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.0064|   0|     nan|

* final LPF:     0.1858

### Increment 10
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999994
|  1  |   0  |  -1   |5.419e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.1427|   0|     nan|

* final LPF:     0.1743

### Increment 11
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999994
|  1  |   0  |  -1   |5.084e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.2730|   0|     nan|

* final LPF:     0.1525

### Increment 12
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999994
|  1  |   0  |  -1   |4.437e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.3898|   0|     nan|

* final LPF:     0.1213

### Increment 13
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999994
|  1  |   0  |  -1   |3.465e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.4850|   0|     nan|

* final LPF:    0.08251

### Increment 14
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999994
|  1  |   0  |  -1   |2.208e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.5510|   0|     nan|

* final LPF:    0.03843

### Increment 15
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999994
|  1  |   0  |  -1   |7.524e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.5822|   0|     nan|

* final LPF:  -0.008139

### Increment 16
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |7.734e-04|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.5755|   0|     nan|

* final LPF:   -0.05418

### Increment 17
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |2.227e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.5318|   0|     nan|

* final LPF:   -0.09672

### Increment 18
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |3.481e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.4549|   0|     nan|

* final LPF:    -0.1331

### Increment 19
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |4.448e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.3513|   0|     nan|

* final LPF:    -0.1612

### Increment 20
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |5.091e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.2289|   0|     nan|

* final LPF:    -0.1795

### Increment 21
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |5.421e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2| -0.0957|   0|     nan|

* final LPF:    -0.1872

### Increment 22
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |5.482e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.0412|   0|     nan|

* final LPF:    -0.1839

### Increment 23
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |5.335e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.1760|   0|     nan|

* final LPF:    -0.1698

### Increment 24
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |5.044e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.3047|   0|     nan|

* final LPF:    -0.1454

### Increment 25
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |4.664e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.4246|   0|     nan|

* final LPF:    -0.1115

### Increment 26
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |4.242e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.5342|   0|     nan|

* final LPF:   -0.06873

### Increment 27
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |3.810e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.6330|   0|     nan|

* final LPF:   -0.01809

### Increment 28
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -0.9999999999999981
|  1  |   0  |  -1   |3.392e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.7213|   0|     nan|

* final LPF:    0.03961

### Increment 29
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |3.000e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.7995|   0|     nan|

* final LPF:     0.1036

### Increment 30
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |2.642e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.8685|   0|     nan|

* final LPF:      0.173

### Increment 31
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |2.320e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.9291|   0|     nan|

* final LPF:     0.2474

### Increment 32
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
1 -1.0000000000000009
|  1  |   0  |  -1   |2.034e-03|   1|      -1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |0.000e+00|    |        |    |        |    |        |
|     |   2  |       |0.000e+00|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   3  |  -1   |0.000e+00|   1| -1.0000|   2|  0.9823|   0|     nan|

* final LPF:      0.326

### Increment 33
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
2 1.0066217668212702
|  1  |   0  |  -1   |1.782e-03|   2|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |7.172e-07|    |        |    |        |    |        |
|     |   2  |       |1.197e-13|    |        |    |        |    |        |
|     |   3  |       |5.551e-17|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   2   |5.551e-17|   2|  1.0000|   1| -0.9725|   0|     nan|

* final LPF:      0.406

### Increment 34
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
2 1.0000000000000002
|  1  |   0  |   2   |1.427e-03|   2|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |3.905e-07|    |        |    |        |    |        |
|     |   2  |       |2.920e-14|    |        |    |        |    |        |
|     |   3  |       |1.665e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   2   |1.665e-16|   2|  1.0000|   1| -0.9368|   0|     nan|

* final LPF:      0.486

### Increment 35
|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
2 0.9999999999999994
|  1  |   0  |   2   |1.182e-03|   2|       1|    |        |    |        |

|Cycle|NR-It.|Control| Norm(g) |i(1)|Value   |i(2)|Value   |i(3)|Value   |
|:---:|:----:|:-----:|:-------:|:--:|:------:|:--:|:------:|:--:|:------:|
|     |   1  |       |2.248e-07|    |        |    |        |    |        |
|     |   2  |       |7.994e-15|    |        |    |        |    |        |
|     |   3  |       |1.110e-16|    |        |    |        |    |        |
|total| sum  | used  |  final  |    | final  |    | final  |    | final  |
|  1  |   4  |   2   |1.110e-16|   2|  1.0000|   1| -0.9083|   0|     nan|

* final LPF:      0.566
* EXIT 1: Job stopped - max value of control component reached.
\pagebreak
 

### Create result object from analysis results for step   1

    write result   1/ 35 (LPF:    0.01393)
    write result   2/ 35 (LPF:    0.03213)
    write result   3/ 35 (LPF:    0.05548)
    write result   4/ 35 (LPF:    0.08456)
    write result   5/ 35 (LPF:     0.1189)
    write result   6/ 35 (LPF:      0.155)
    write result   7/ 35 (LPF:     0.1759)
    write result   8/ 35 (LPF:     0.1863)
    write result   9/ 35 (LPF:     0.1858)
    write result  10/ 35 (LPF:     0.1743)
    write result  11/ 35 (LPF:     0.1525)
    write result  12/ 35 (LPF:     0.1213)
    write result  13/ 35 (LPF:    0.08251)
    write result  14/ 35 (LPF:    0.03843)
    write result  15/ 35 (LPF:  -0.008139)
    write result  16/ 35 (LPF:   -0.05418)
    write result  17/ 35 (LPF:   -0.09672)
    write result  18/ 35 (LPF:    -0.1331)
    write result  19/ 35 (LPF:    -0.1612)
    write result  20/ 35 (LPF:    -0.1795)
    write result  21/ 35 (LPF:    -0.1872)
    write result  22/ 35 (LPF:    -0.1839)
    write result  23/ 35 (LPF:    -0.1698)
    write result  24/ 35 (LPF:    -0.1454)
    write result  25/ 35 (LPF:    -0.1115)
    write result  26/ 35 (LPF:   -0.06873)
    write result  27/ 35 (LPF:   -0.01809)
    write result  28/ 35 (LPF:    0.03961)
    write result  29/ 35 (LPF:     0.1036)
    write result  30/ 35 (LPF:      0.173)
    write result  31/ 35 (LPF:     0.2474)
    write result  32/ 35 (LPF:      0.326)
    write result  33/ 35 (LPF:      0.406)
    write result  34/ 35 (LPF:      0.486)
    write result  35/ 35 (LPF:      0.566)

End of Step 1
\pagebreak
 

## Job duration
Time measurement for execution times of "Model.build()" and "Model.run()".

    total  cpu time "build":      0.001 seconds
    total wall time "build":      0.001 seconds

    total  cpu time "run":        0.202 seconds
    total wall time "run":        0.197 seconds

