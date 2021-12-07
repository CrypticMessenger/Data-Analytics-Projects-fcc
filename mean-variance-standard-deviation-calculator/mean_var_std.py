import numpy as np
def calculate(l):
  if len(l) != 9:
    raise ValueError("List must contain nine numbers.")
  arr=np.array([l[0:3],l[3:6],l[6:9]])
  k=['mean','variance','standard deviation','max','min','sum']
  v=[]
  l1=[np.mean(arr,axis=0).tolist(),np.mean(arr,axis=1).tolist(),np.mean(arr)]
  l3=[np.std(arr,axis=0).tolist(),np.std(arr,axis=1).tolist(),np.std(arr)]
  l2=[np.var(arr,axis=0).tolist(),np.var(arr,axis=1).tolist(),np.var(arr)]
  l4=[np.amax(arr,axis=0).tolist(),np.amax(arr,axis=1).tolist(),np.amax(arr)]
  l5=[np.amin(arr,axis=0).tolist(),np.amin(arr,axis=1).tolist(),np.amin(arr)]
  l6=[np.sum(arr,axis=0).tolist(),np.sum(arr,axis=1).tolist(),np.sum(arr)]
  v.append(l1)
  v.append(l2)
  v.append(l3)
  v.append(l4)
  v.append(l5)
  v.append(l6)
  calculations=dict(zip(k,v))
  return (calculations)
