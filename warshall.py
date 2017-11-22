
# coding: utf-8

import numpy as np

class B_transitivity:
    def __init__(self, B,n):
        self.B = B
        self.n = n
    def warshall(self,B,n):
        A = B.copy()
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    A[i][j] = A[i][j] or (A[i][k] and A[k][j])
        return A
    
    def kleen_closure(self, B_plus, I):
        B_star = np.logical_or(I,B_plus)
        return B_star.astype(int)
                

def main():
    #Creating an 8 x 8 matrix of 0s and 1s
    nodes = raw_input('Enter the number of nodes in the graph: ')
    nodes = int(nodes)
    B = np.zeros((nodes,nodes))
    for i in xrange(len(B)):
        mystr = raw_input('Enter the %d th row of the matrix: \n'%(i+1))
        B[i] = np.array(list(mystr))

    n=nodes # Number of vertices

    #Applying Warshall's algorithm to B to get the transitivity closure for B, i.e, B+

    B_trans = B_transitivity(B,n)
    I = np.identity(n)               #Identity matrix

    B_plus = B_trans.warshall(B,n)
    print '\n'
    print 'The transitivity closure for B is B+, given by:\n'
    print '=================================================\n'
    print B_plus
    print '\n\n'
    print "Kleen's closure for B is B*, given by:\n"
    print '=================================================\n'
    print B_trans.kleen_closure(B_plus,I)
    
    return


if __name__ == "__main__":
    main()



