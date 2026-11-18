import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import factorized

# Parameters
N, L, Uwall, Re = 51, 1.0, 1.0, 100.0
h = L/(N-1)
dt, tol, max_steps = 5e-4, 1e-8, 150000
ni = N-2

# Poisson matrix for Laplacian(psi) = -omega
A = lil_matrix((ni*ni, ni*ni))
for j in range(ni):
    for i in range(ni):
        k = j*ni+i
        A[k,k] = -4
        if i > 0: A[k,k-1] = 1
        if i < ni-1: A[k,k+1] = 1
        if j > 0: A[k,k-ni] = 1
        if j < ni-1: A[k,k+ni] = 1
solve_poisson = factorized(A.tocsc())

psi = np.zeros((N,N))
omega = np.zeros((N,N))
u = np.zeros((N,N))
v = np.zeros((N,N))

for step in range(max_steps):
    psi[1:-1,1:-1] = solve_poisson(
        -omega[1:-1,1:-1].ravel()*h**2
    ).reshape((ni,ni))

    u[1:-1,1:-1] = (psi[2:,1:-1]-psi[:-2,1:-1])/(2*h)
    v[1:-1,1:-1] = -(psi[1:-1,2:]-psi[1:-1,:-2])/(2*h)

    # Vorticity at walls; left wall moves upward
    omega[:,0] = -2*(psi[:,1]-psi[:,0]+h*Uwall)/h**2
    omega[:,-1] = -2*(psi[:,-2]-psi[:,-1])/h**2
    omega[0,:] = -2*(psi[1,:]-psi[0,:])/h**2
    omega[-1,:] = -2*(psi[-2,:]-psi[-1,:])/h**2

    omega[0,0] = 0.5*(omega[0,1]+omega[1,0])
    omega[-1,0] = 0.5*(omega[-1,1]+omega[-2,0])
    omega[0,-1] = 0.5*(omega[0,-2]+omega[1,-1])
    omega[-1,-1] = 0.5*(omega[-1,-2]+omega[-2,-1])

    w = omega
    wx = np.where(u[1:-1,1:-1] >= 0,
        (w[1:-1,1:-1]-w[1:-1,:-2])/h,
        (w[1:-1,2:]-w[1:-1,1:-1])/h)
    wy = np.where(v[1:-1,1:-1] >= 0,
        (w[1:-1,1:-1]-w[:-2,1:-1])/h,
        (w[2:,1:-1]-w[1:-1,1:-1])/h)
    lap = (w[1:-1,2:]+w[1:-1,:-2]+w[2:,1:-1]+
           w[:-2,1:-1]-4*w[1:-1,1:-1])/h**2

    wnew = w[1:-1,1:-1] + dt*(
        -u[1:-1,1:-1]*wx-v[1:-1,1:-1]*wy+lap/Re)
    err = np.max(np.abs(wnew-w[1:-1,1:-1]))
    omega[1:-1,1:-1] = wnew

    if err < tol and step > 1000:
        break

# Final fields
psi[1:-1,1:-1] = solve_poisson(
    -omega[1:-1,1:-1].ravel()*h**2
).reshape((ni,ni))
u[1:-1,1:-1] = (psi[2:,1:-1]-psi[:-2,1:-1])/(2*h)
v[1:-1,1:-1] = -(psi[1:-1,2:]-psi[1:-1,:-2])/(2*h)
v[:,0] = Uwall
v[:,-1] = 0.0
u[0,:] = 0.0
u[-1,:] = 0.0

mid = N//2
profile = v[mid,:]
peak = np.argmin(profile)
print("Iterations:", step)
print("Final maximum vorticity update:", err)
print("u at centre:", u[mid,mid])
print("v at centre:", v[mid,mid])
print("Maximum reverse-flow speed:", abs(profile[peak]))
print("Distance from moving wall:", peak*h)

x = np.linspace(0,L,N)
y = np.linspace(0,L,N)
X,Y = np.meshgrid(x,y)
fig,ax = plt.subplots(1,2,figsize=(11,4))
c = ax[0].contourf(X,Y,v,levels=25)
fig.colorbar(c,ax=ax[0],label="v")
ax[0].streamplot(x,y,u,v,color="k",density=1.1)
ax[0].set(title="Vertical velocity and streamlines",xlabel="x",ylabel="y")
ax[0].set_aspect("equal")
ax[1].plot(x,profile)
ax[1].axhline(0,color="k",linewidth=.7)
ax[1].plot(x[peak],profile[peak],"ro")
ax[1].set(title="v along y = 0.5",xlabel="x from moving wall",ylabel="v")
ax[1].grid()
fig.tight_layout()
plt.show()