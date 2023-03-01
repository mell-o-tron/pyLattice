# pyLattice
A simple tool for visualizing and animating 2D lattices (i.e. discrete subgroups of $\mathbb R^2$)

## Usage

### Drawing a lattice

You can use the `drawLattice` function to draw a lattice of the form $M(\mathbb Z^2)$, where $M$ is a matrix with integer values. E.g.:

```python
M = np.array([[1, 0], [0, 1]])
asyncio.run(drawLattice (M, screen, window_size, res, (1,1,0)))

```

Will draw the $\mathbb Z^2$ lattice. The `(1,1,0)` specifies a color with values 0 to 1, in this case the lattice will be drawn in yellow. The "res"(-olution) is controlled with the mouse wheel, which can be used to "zoom in". As this is written in Python, you'll notice that, if you zoom far enough, the performance of the animations will be absolute garbage.

### Gaussian SVP-2 algorithm 

Call the following function:

```python
draw_gauss (v1_arg, v2_arg, interval, res, screen, winsize)
```
Where `v1_arg` and `v2_arg` are the vectors of the base, and `interval` is the duration of an animation step in milliseconds.

## Previews
Visualization of the Gaussian algorithm for the Shortest Vector Problem with norm 2
![preview](https://github.com/mell-o-tron/pyLattice/blob/main/gauss.png)

A visualization of a lattice and sublattice
![preview](https://github.com/mell-o-tron/pyLattice/blob/main/sublattice.png)
