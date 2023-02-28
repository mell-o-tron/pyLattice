# pyLattice
A simple tool for visualizing and animating 2D lattices (i.e. integer linear combinations of vectors $\in \mathbb Z^2$)

## Usage
You can use the `drawLattice` function to draw a lattice of the form $M(\mathbb Z^2)$, where $M$ is a matrix with integer values. E.g.:

```python
M = np.array([[1, 0], [0, 1]])
asyncio.run(drawLattice (M, screen, window_size, res, (1,1,0)))

```

Will draw the $\mathbb Z^2$ lattice. The `(1,1,0)` specifies a color with values 0 to 1, in this case the lattice will be drawn in yellow. The "res" is controlled with the mouse wheel, which can be used to "zoom in". As this is written in Python, you'll notice that, if you zoom far enough, the performance of the animations will be absolute garbage.

## Previews
Visualization of the Gaussian algorithm for the Shortest Vector Problem with norm 2
![preview](https://github.com/mell-o-tron/pyLattice/blob/main/gauss.png)

A visualization of a lattice and sublattice
![preview](https://github.com/mell-o-tron/pyLattice/blob/main/sublattice.png)
