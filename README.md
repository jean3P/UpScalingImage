# Up-scaling Image

Implementation of the up-scaling algorithm (python) for the Document Image Analysis course.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) 

Two algorithms have been implemented that scale the image by a factor of two:

 **- Nearest Neighbour**

 **- Bilineal interpolation**
 
## Tech Stack
 **Programming language:** Python3

 **Programming libraries:** OpenCV, Numpy
 
## Run Locally

Clone the project
```bash
  git clone https://github.com/jean3P/UpScalingImage.git
```

Go to the project directory
```bash
  cd UpScalingImage/src
```

Run with Python
```bash
  python Main.py
```
## Results directories
Nearest neigbour
```bash
  cd UpScalingImage/nearestNeghbour
```

Bilineal interpolation
```bash
  cd UpScalingImage/bilinearInterpolation
```

## Statistics

| Algorithm              |   300x450   |   500x750    |   1850x2750    |
|:-----------------------|:-----------:|:------------:|:--------------:|
| Nearest neighbour      | 0.003757 s  |  0.012408 s  |   0.534406 s    |
| Bilineal interpolation | 3.217833 s  |  8.427347 s  |  100.843575 s  |

## Author
- [PEREYRA PRINCIPE Jean Pool](https://github.com/jean3P)

## License

[MIT](https://choosealicense.com/licenses/mit/)