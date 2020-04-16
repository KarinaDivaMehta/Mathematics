# Motivations
1. solving simultaneous equations 
2. the optimization problem of fitting some data with an equation with some fitting parameters

What we want to do the most in machine learning is the second motivation. We have a guessing character vector and we want to fit it to the graph and we move the vector to see the overlap area change. And we find the optimal solution.

These kind of problems are going to involve vectors and possibly some calculus.

# Vectors
## operations
1. Length of vector

2. Dot Product
    
    denote projection vector of s onto r adj
    $$
    r.s = |r|*|s|*cos $\theta$ = |r| * adj\\
    |adj| = r.s/|r|\\
    adj = r.s/|r|<sup>2</sup>*r
    $$
    
3. Changing basis
* Basis are a set of vectors that 
    1. are not linear combinations of each other
    2. span the space
    
* How to change basis:
    assume v<sub>1</sub> and v<sub>2</sub> are vectors in my basis
    u<sub>1</sub> is vector in v<sub>1</sub>, v<sub>2</sub> basis (v<sub>1</sub> v<sub>2</sub> are linear independent)
    $$
    [v_1, v_2] * u_1 = u_2
    $$
    
    
    Then u<sub>2</sub> is the vector in my basis
    Similarly,
    $$
    [v_1, v_2]^{-1} * u_2 = u_1
    $$
    
    
    
    
* Application of Chaning basis:
  
  Assume we have several points dropping near a line. And the line has some angle with the horizontal axis. Then we can change the basis so that we can more efficiently figure out how far is the point to the line.

# Matrix

## Overview

Matrix transform a vector to another place in space (rotate, shear, inverse)

Assume that a vector v on basis (e<sub>1</sub>, e<sub>2</sub>, e<sub>3</sub>) and it will be transformed into another.vector if the new basis is (u<sub>1</sub>, u<sub>2</sub>, u<sub>3</sub>) by [u<sub>1</sub>, u<sub>2</sub>, u<sub>3</sub>] * v

## Determinant: The area of spanning space of the vectors

If determinant is 0 then the vectors are not linear independent.
$$
Denote: C = \left[
\begin{matrix}
a & b\\
c & d
\end{matrix}
\right] \\
det(C) = ad-bc \\
inverse(C) = 
\left[
\begin{matrix}
d & -b\\
-c & a
\end{matrix}
\right]/det(C)
$$
If determinant of a matrix is 0, and we use this matrix to transform a vector, this operation cannot be undone as there is no inverse of the matrix.

##Matrix change basis

Bear's basis vectors matrix in my view(B) * Bear's vector(u) = my vector(v)

Then B^-1 is my basis in Bear's world

If you want to do a transformation (R) to vecotr v in your basis and you want to know how it transforms in bear's basis

B^-1.R.B.v

###Orthogonal Basis

Orthogonal basis is important because in such basis A<sup>-1</sup> = A<sup>T</sup>
How to change basis to be orthogonal to each other: Gram–Schmidt process
u<sub>i</sub> = v<sub>i</sub> - (v<sub>i</sub> . e<sub>j</sub>)*e<sub>j</sub> (0<=j<i)

When we found it so hard to transform r to r`, we can first change basis to E then at the E basis do the transformation and finally get back to our basis. E.T<sub>E</sub>.E<sup>-1</sup>.r = r'

r.E<sup>-1</sup> => r<sub>E</sub>

r<sub>E</sub>.T<sub>E</sub> => r'<sub>E</sub>

r'<sub>E</sub>.E => r'

Example: We want to know a vector r' which is a reflection in mirror of r. We know 2 vectors (v<sub>1</sub>, v<sub>2</sub>) in the mirror (linear independent) and another vector v<sub>3</sub> not in the plane of mirror

We first use Gram-Schmidt process to get the mirror vectors e<sub>1</sub> e<sub>2</sub> and e<sub>3</sub> perpendicular to the plane. Then we know that the transformation at [e<sub>1</sub>, e<sub>2</sub>, e<sub>3</sub>] basis is : (as is a reflection of mirror)
$$
\left[
\begin{matrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & -1
\end{matrix}
\right]
$$
So what we do here is to use the above formula, here the E is (e1, e2, e3) to do the transformation. As the basis are all perpendicular to each other, E<sup>-1</sup> = E<sup>T</sup> so it will be more easier.

# Eigenvalues and Eigenvectors

## Overview

Eigen means characteristics 

Eigenvectors : After a transformation, the vecotrs that are still lays on the same span

Eigenvalues: How much the length of eigenvectors are changed

So for eigenvectors

Av = $\lambda$v where $\lambda$ is a constant

So det(A-$\lambda$I) = 0

## What we want to solve

We have a vector v and a tranformation matrix T. We want to transform the vector n times namely T<sup>n</sup> . v

It will be slow to calculate the matrix product for n times so we now use eigenvectors.

In the basis of eigenvectos, a transformation of T is simply a scaling where the scaling = $\lambda$

We denote the eigenvecots transformation matrix C and the $\lambda$ matrix D

As D is like
$$
\left[
\begin{matrix}
\lambda_1 & 0 & 0\\
0 & \lambda_2 & 0\\
0 & 0 & \lambda_3
\end{matrix}
\right]
$$
Then
$$
D^n=\left[
\begin{matrix}
\lambda_1^n & 0 & 0\\
0 & \lambda_2^n & 0\\
0 & 0 & \lambda_3^n
\end{matrix}
\right]
$$


T<sup>n</sup> . v = CD<sup>n</sup>C<sup>-1</sup>

