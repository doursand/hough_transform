# Hough Transform - Line Detection
[![Build Status](https://travis-ci.org/alyssaq/hough_transform.svg?branch=master)](https://travis-ci.org/alyssaq/hough_transform)

Python implementation of hough transform for detecting lines in images.    
Explanation of how the hough transform works in my blog post: [Understanding Hough Transform](https://alyssaq.github.io/2014/understanding-hough-transform)
Implemented code into an ht class aiming to handle hough transform and allowing to visualize resulting lines in (x,y) space

## Requirements
* Tested on Python 3.6
* `pip install -r requirements.txt`

## Usage
```py
python ht.py
```
## Sample 
![hough transform image](imgs/output.png)

## Tests
```py
python hough_transform_test.py
```

## Resources
* OpenCV's hough transform documentation: 
<http://docs.opencv.org/doc/tutorials/imgproc/imgtrans/hough_lines/hough_lines.html>
* EGGN 512 hough transform lecture in 3 parts:
<https://www.youtube.com/watch?v=uDB2qGqnQ1g>
