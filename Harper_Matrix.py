import numpy as np

def H_k(p,q,kx,ky):
    
    alpha = p/q
    
    M = np.zeros((q,q), dtype=complex)
    
    for i in range(0,q):
        M[i,i] = 2*np.cos(ky-2*np.pi*alpha*i)
        if i==q-1: 
            M[i,i-1]=np.exp(-q*1.j*kx)
        elif i==0: 
            M[i,i+1]=np.exp(-q*1.j*kx)
        else: 
            M[i,i-1]=np.exp(-q*1.j*kx)
            M[i,i+1]=np.exp(-q*1.j*kx)
            
    if q==2:
        M[0,q-1] = 1+np.exp(-q*1.j*kx)
        M[q-1,0] = 1+np.exp(q*1.j*kx)
    else:
        M[0,q-1] = np.exp(-q*1.j*kx)
        M[q-1,0] = np.exp(q*1.j*kx)
        
    return M