# Laser Reflection Pattern from a Vibrating Circular Membrane

## Physical System
Consider a circular membrane of radius $$R$$ vibrating under tension. A laser reflects off a point $$(r_0, \theta_0)$$ on the membrane and projects onto a screen at distance $$L$$. We derive the pattern traced by the laser during vibration.

## Governance Equation
The transverse displacement $$z(r,\theta,t)$$ satisfies the wave equation in polar coordinates:
$$
\nabla^2 z = \frac{1}{v^2} \frac{\partial^2 z}{\partial t^2}
$$
For time-harmonic solutions, this reduces to the Helmholtz equation:
$$
\left(\nabla^2 + k^2\right) z = 0
$$

## General Solution
The complete solution is a linear combination of normal modes:
$$
z(r,\theta,t) = \sum_{m=0}^\infty \sum_{n=1}^\infty A_{mn} J_m\left(\frac{\alpha_{mn}r}{R}\right) \cos(m\theta + \phi_{mn}) \cos(\omega_{mn}t + \psi_{mn})
$$

Where:
- $$J_m$$: Bessel function of first kind, order $$m$$
- $$\alpha_{mn}$$: $$n$$-th positive root of $$J_m$$
- $$\omega_{mn} = c\frac{\alpha_{mn}}{R}$$: Mode frequency
- $$A_{mn}$$: Mode amplitude
- $$\phi_{mn}, \psi_{mn}$$: Phase constants

## Reflection Geometry
The surface normal vector $$\mathbf{n}$$ determines reflection direction. For small displacements ($$|\nabla z| \ll 1$$):
$$
\mathbf{n} \approx \left(-\frac{\partial z}{\partial x}, -\frac{\partial z}{\partial y}, 1\right)
$$

### Incident Laser
Assume vertical incidence (along $$\hat{z}$$):
$$
\mathbf{v}_i = (0,0,1)
$$

### Reflected Direction
Using the law of reflection:
$$
\mathbf{v}_r = \mathbf{v}_i - 2\frac{\mathbf{v}_i \cdot \mathbf{n}}{\|\mathbf{n}\|^2}\mathbf{n} \approx (-2\frac{\partial z}{\partial x}, -2\frac{\partial z}{\partial y}, 1)
$$

## Screen Projection
At screen distance $$L$$, coordinates become:
$$
x_{\text{screen}} = -2L \frac{\partial z}{\partial x}\bigg|_{\substack{r=r_0\\ \theta=\theta_0}},\quad y_{\text{screen}} = -2L \frac{\partial z}{\partial y}\bigg|_{\substack{r=r_0\\ \theta=\theta_0}}
$$

## Gradient Calculation
We need $$\partial z/\partial x$$ and $$\partial z/\partial y$$ at $$(r_0, \theta_0)$$.

### Polar Gradient Components
First compute polar derivatives:

**Radial derivative**:
$$
\begin{aligned}
\frac{\partial z}{\partial r} &= \sum_{m,n} A_{mn} \frac{\alpha_{mn}}{R} J_m'\left(\frac{\alpha_{mn}r_0}{R}\right) \cos(m\theta_0 + \phi_{mn}) \cos(\omega_{mn}t + \psi_{mn}) \\
J_m'(x) &= \frac{1}{2}[J_{m-1}(x) - J_{m+1}(x)] \quad \text{(Bessel derivative identity)}
\end{aligned}
$$

**Angular derivative**:
$$
\frac{\partial z}{\partial \theta} = -\sum_{m,n} A_{mn} m J_m\left(\frac{\alpha_{mn}r_0}{R}\right) \sin(m\theta_0 + \phi_{mn}) \cos(\omega_{mn}t + \psi_{mn})
$$

### Cartesian Conversion
Transform to Cartesian coordinates:
$$
\begin{aligned}
\frac{\partial z}{\partial x} &= \frac{\partial z}{\partial r}\cos\theta_0 - \frac{1}{r_0}\frac{\partial z}{\partial \theta}\sin\theta_0 \\
\frac{\partial z}{\partial y} &= \frac{\partial z}{\partial r}\sin\theta_0 + \frac{1}{r_0}\frac{\partial z}{\partial \theta}\cos\theta_0
\end{aligned}
$$

## Final Parametric Equations
Substitute into screen coordinates:

**X-coordinate**:
$$
\begin{aligned}
x_{\text{screen}}(t) &= -2L \sum_{m,n} A_{mn} \cos(\omega_{mn}t + \psi_{mn}) \Biggl[ \frac{\alpha_{mn}}{R} J_m'\left(\frac{\alpha_{mn}r_0}{R}\right) \cos\theta_0 \cos(m\theta_0 + \phi_{mn}) \\
&\quad + \frac{m}{r_0} J_m\left(\frac{\alpha_{mn}r_0}{R}\right) \sin\theta_0 \sin(m\theta_0 + \phi_{mn}) \Biggr]
\end{aligned}
$$

**Y-coordinate**:
$$
\begin{aligned}
y_{\text{screen}}(t) &= -2L \sum_{m,n} A_{mn} \cos(\omega_{mn}t + \psi_{mn}) \Biggl[ \frac{\alpha_{mn}}{R} J_m'\left(\frac{\alpha_{mn}r_0}{R}\right) \sin\theta_0 \cos(m\theta_0 + \phi_{mn}) \\
&\quad - \frac{m}{r_0} J_m\left(\frac{\alpha_{mn}r_0}{R}\right) \cos\theta_0 \sin(m\theta_0 + \phi_{mn}) \Biggr]
\end{aligned}
$$

We introduce the following constants to group the constant terms:

$$
B_{mn}^x = \frac{\alpha_{mn}}{R} J_m'\!\left(\frac{\alpha_{mn}r_0}{R}\right) \cos\theta_0,\quad
C_{mn}^x = \frac{m}{r_0} J_m\!\left(\frac{\alpha_{mn}r_0}{R}\right) \sin\theta_0,
$$
$$
B_{mn}^y = \frac{\alpha_{mn}}{R} J_m'\!\left(\frac{\alpha_{mn}r_0}{R}\right) \sin\theta_0,\quad
C_{mn}^y = \frac{m}{r_0} J_m\!\left(\frac{\alpha_{mn}r_0}{R}\right) \cos\theta_0.
$$

With these definitions, the equations can be rewritten as:

$$
\begin{aligned}
x_{\text{screen}}(t) &= -2L \sum_{m,n} A_{mn} \cos(\omega_{mn}t + \psi_{mn}) \Bigl[ B_{mn}^x \cos(m\theta_0 + \phi_{mn}) + C_{mn}^x \sin(m\theta_0 + \phi_{mn}) \Bigr], \\
y_{\text{screen}}(t) &= -2L \sum_{m,n} A_{mn} \cos(\omega_{mn}t + \psi_{mn}) \Bigl[ B_{mn}^y \cos(m\theta_0 + \phi_{mn}) - C_{mn}^y \sin(m\theta_0 + \phi_{mn}) \Bigr].
\end{aligned}
$$

We define the following constants that group all time-independent terms:

$$
D_{mn}^x = A_{mn} \bigl[ B_{mn}^x \cos(m\theta_0 + \phi_{mn}) + C_{mn}^x \sin(m\theta_0 + \phi_{mn}) \bigr],
$$
$$
D_{mn}^y = A_{mn} \bigl[ B_{mn}^y \cos(m\theta_0 + \phi_{mn}) - C_{mn}^y \sin(m\theta_0 + \phi_{mn}) \bigr].
$$

Substituting these constants into the original equations:

$$
x_{\text{screen}}(t) = -2L \sum_{m,n} D_{mn}^x \cos(\omega_{mn}t + \psi_{mn}),
$$

$$
y_{\text{screen}}(t) = -2L \sum_{m,n} D_{mn}^y \cos(\omega_{mn}t + \psi_{mn}).
$$

These equations show that the trajectory of the laser point on the screen is a combination of oscillations in $$x$$ and $$y$$, where the coefficients $$D_{mn}^x$$ and $$D_{mn}^y$$ encapsulate all spatial and modal dependencies, leaving the temporal evolution governed solely by the terms $$\cos(\omega_{mn}t + \psi_{mn})$$.

## Key Observations
1. **Mode Coupling**: Each mode contributes terms proportional to $$\omega_{mn}t + \psi_{mn}$$
2. **Time Dependence**: $$\cos(\omega_{mn}t + \psi_{mn})$$ creates time modulation
3. **Frequency Mixing**: For multiple modes, cross terms generate:
   $$
   \cos(\omega_{pq}t)\cos(\omega_{rs}t) \propto \cos[(\omega_{pq} \pm \omega_{rs})t]
   $$
4. **Lissajous Figures**: When $$\omega_{pq}/\omega_{rs}$$ is rational, curves close; irrational ratios produce non-repeating patterns

## Special Case: Single Mode
For a single $$(m,n)$$ mode:
$$
\begin{cases}
x_{\text{screen}}(t) = C_x \cos(\omega t + \psi) \\
y_{\text{screen}}(t) = C_y \cos(\omega t + \psi)
\end{cases}
$$
This traces an ellipse. Adding modes breaks this symmetry.
