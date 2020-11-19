import numpy as np
class HopfildNN:
    def learn(self,data):
        d= np.array(data)
        W = None
        for obr in d:
            obr = np.array([obr])
            if W is None:
                W = np.dot(obr.T,obr)
            else:
                W+=np.dot(obr.T,obr)
            for i in range(len(W)):
                W[i][i] = 0