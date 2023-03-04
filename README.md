# Up-scaling Image

Implementation of the up-scaling algorithm (python) for the Document Image Analysis course.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) 

Two algorithms have been implemented that scale the image by a factor of two:

 **- Nearest Neighbour**

 **- Bilineal interpolation**
 
## Tech Stack
 **Programming language:** Python3

 **Programming libraries:** Pillow, Numpy
 
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

# Assignment 2

## Nearest Neighbour

### Visually: 
In the figure, it can be appreciated that the results obtained using the Nearest Neigbour algorithm are not good, because the edges are jagged and the image looks distorted and pixelated (aliasing). The same happens with the other images. 

[![V-1.png](https://i.postimg.cc/wvZq6Zys/V-1.png)](https://postimg.cc/TLjM0kcR) 

### Subtraction

 **- Normal Subtraction:** The Figure is the result of a normal subtraction. The variety of colours that can be seen is because the type of the image is in unit8 and when a subtraction is made, any negative value is re-circled to 255 because this format cannot handle negative values. For example if the value of the subtraction is -1, its value would be 254. In the figure there is a variety of colours, this gives the information that there are many more values belonging to the scaled image that are greater than the original image. 

[![Diff-1.png](https://i.postimg.cc/d1LW2SW6/Diff-1.png)](https://postimg.cc/qhHX0QH6)

 **- Subtraction where negative values are equal to 0:** This Figure is the result of equating the negative values to 0 (0 has the colour black) so the pixels that can be seen are the result of subtraction where the pixel values of the original image are greater than those of the scaled image.

[![Diff-2.png](https://i.postimg.cc/63X3RD5J/Diff-2.png)](https://postimg.cc/CZcSprqm)

 **- Statistics:** The differences can be seen more clearly, the number of equal pixels does not exceed 10\%, this means that the scaled image has more differences than hits, therefore the Nearest Neighbour, it is true that it has a fast execution time, but it loses a lot of precision.

| Measurement in %                                                  | 600x900 | 1000x1500 | 3700x5500 |
|:------------------------------------------------------------------|:-------:|:---------:|:---------:|
| Equal pixels in both images                                       |   3.3   |   3.62    |   6.98    |
| Pixels of the original image that are greater than the scaled one |  49.34  |   48.03   |   45.89   |
| Pixels of the scaled image that are greater than the original one |  47.36  |   48.36   |   47.13   |

### Signal Noise Ratio
Is used in imaging as a physical measure of the sensitivity of a (digital or film) imaging system. Industry standards measure and define sensitivity in terms of the ISO film speed equivalent:

**- 32.04 dB = excellent image quality and SNR**

**- 20 dB = acceptable image quality**

It can be clearly seen that there is a low SNR value for all images, which means that there is too much noise in the scaled images.

| Image Size |   NSR    |
|:-----------|:--------:|
| 600x900    | 13.12 dB |
| 1000x1500  | 12.42 dB |
| 3700x55000 | 14.01 dB |

## Bilienear Interpolation

### Visually
It can be seen in the figure that there is undesirable smoothing in the details, and it is irregular.

[![V-2.png](https://i.postimg.cc/PJYX3y3s/V-2.png)](https://postimg.cc/5Q9WjBWn)

### Subtraction
At the time of subtraction, the results are similar to Nearest Neighbour. The table shows that the number of equal pixels has only increased slightly, but there is still a large loss of precision.

| Measurement in %                                                  | 600x900 | 1000x1500 | 3700x5500 |
|:------------------------------------------------------------------|:-------:|:---------:|:---------:|
| Equal pixels in both images                                       |  3.82   |   4.33    |   8.42    |
| Pixels of the original image that are greater than the scaled one |  50.56  |   48.86   |   47.05   |
| Pixels of the scaled image that are greater than the original one |  45.61  |   46.81   |   44.54   |

### Signal Noise Ratio
As can be seen in the table the SNR values show that there is still too much noise.

| Image Size |   NSR    |
|:-----------|:--------:|
| 600x900    | 13.25 dB |
| 1000x1500  | 12.66 dB |
| 3700x55000 | 14.53 dB |

**- Python file:** A new Main_Subtraction.py script has been added, which performs the necessary calculation and displays the statistics.

**- Future improvements:** The quality of the scaled images could be improved by adding a spatial domain filter or bicubic interpolation could be tried.


## Author

- [PEREYRA PRINCIPE Jean Pool](https://github.com/jean3P)


## License

[MIT](https://choosealicense.com/licenses/mit/)