from IPython.parallel import Client
import numpy as np

def rand_det(n):
    """
    A pointless work function. Calculates the detirminant of a random
    positive definite matrix of dimension n
    """
    A = np.random.rand(n,n)
    A = A.T.dot(A)
    return np.linalg.det(A)

client = Client()   
view = client.load_balanced_view()

handles = view.map_async(rand_det, range(0, 1000))

try: 
    handles.wait_interactive(interval=0.1)
except KeyboardInterrupt as e:
    print "aborting"
    handles.abort()
    exit()
 
print handles.get()
client.clear()
