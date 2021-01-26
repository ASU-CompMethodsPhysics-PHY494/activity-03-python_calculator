# Activity 03: Python as a Calculator

https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494//2021/01/26/03_HelloWorld/#activity-python-as-a-calculator

Create a file `solution.py` in which you evaluate the following mathematical expressions and assign them to variables `a`, `b`, ...

(To view the mathematics nicely typeset, view the notebook [README.ipynb](README.ipynb) or as a PDF [README.pdf](README.pdf).)

\begin{align}
a &= -1 + 2  \\
b &= 102 - 201  \\
c &= 12345678987654321 \times 9876543210123456789 \\
d &= 3/2\\
e &= \frac{1}{1 - 0.9^2}\\
f &= 1 + \frac{2}{1} + \frac{2^2}{1\cdot2} + \frac{2^3}{1\cdot2\cdot3} + \frac{2^4}{1 \cdot 2\cdot3\cdot4}\\
g &= -3^4\\
h &= 2 - 5.5\times 10^{-7}\\
i &= 1.672621898\times 10^{-27} \times (3\times10^8)^2\\
j &= \sqrt{2}\\
k &= \sqrt{-1}\\
l &= (1 + 2i) + (-2 + i)\\
m &= \frac{1 + 2i}{2 - i}\\
\end{align}


## Testing

Run the tests locally with

    pytest

In order to perform autograding, `git push` your changes.

## Example

The first line in `solution.py` should be

    a = -1 + 2

