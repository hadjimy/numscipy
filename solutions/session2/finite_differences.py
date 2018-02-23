def get_error(N=50,nomr=2):
    x = np.linspace(-1,1,N)
    f = np.sin(2*np.pi*x)
    df = 2*np.pi*np.cos(2*np.pi*x)

    numdf = np.zeros(N)
    dx = x[1]-x[0]
    numdf[0] = (f[1]-f[0])/dx
    numdf[-1] = (f[-1]-f[-2])/dx
    numdf[1:-1] = (f[2:]-f[:-2])/(2*dx)

    err = dx**(1./norm)*np.linalg.norm(df - numdf,norm)

    return err, dx


grid_pts = [50*x for x in range(1,7)]
err = np.zeros(len(grid_pts))
dx = np.zeros(len(grid_pts))

for i,N in enumerate(grid_pts):
    err[i], dx[i] = get_error(N)

plt.loglog(dx,err,'--b',dx,dx**2,'--r')
