from Harper_Matrix import *
import matplotlib.pyplot as plt

def gcd(a, b): 
    if b == 0: return a
    return gcd(b, a % b)

def plot_butterfly(q_max):
    
    for p in range(1, q_max+1):
        for q in range(1, q_max+1):
            
            if q>p:
                if gcd(p, q) == 1:
                    alpha = p/q
                    y = np.zeros(q)
                    y[:] = alpha
                    
                    x1 = np.linalg.eigvalsh(H_k(p,q,kx=0, ky=0))
                    x2 = np.linalg.eigvalsh(H_k(p,q,kx=np.pi/q, ky=np.pi/q))
                    
                    for i in range(len(x1)):
                        plt.plot([x1[i],x2[i]], y[:2], '-', c="black", markersize=0.1)
                    
                    plt.plot(x1, y, 'o', c="black", markersize=0.1)
                    plt.plot(x2, y, 'o', c="black", markersize=0.1)

    plt.xlabel(r'$\epsilon$', fontsize=15)
    plt.ylabel(r'$\alpha$', fontsize=15)
    plt.title(r'$q=1-$'+str(q_max))  
    
    return 