# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:02:06 2021

@author: thibaut
"""

def mergeSort(A):
    if len(A)>1:
        n = len(A)//2
        B=A[:n]
        C=A[n:]
 # recursive call of mergeSort       
        mergeSort(B)
        mergeSort(C)
        i=0
        j=0
        k=0
 # compare the elements of the two sorted arrays B and  C , and take the smallest       
        while i<len(B) and j<len(C):
            if B[i]<C[j]:
               A[k]=B[i]
               i+=1
            else:
               A[k]=C[j]
               j+=1
            k+=1
# copy the elements remaining in the array B or C not the both            
        while i<len(B):
            A[k]=B[i]
            i+=1
            k+=1
        while j<len(C):
            A[k]=C[j]
            j+=1
            k+=1
A=[1, 20, 6, 4, 5 ]
mergeSort(A)      
print(A) 