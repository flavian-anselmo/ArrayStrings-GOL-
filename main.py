"""
1. Reverse Array In-place
Write a function reverseArray(A) that takes in an array A and reverses it, without using another array or collection data structure; in-place.

Example:

A = [10, 5, 6, 9] reverseArray(A) A // [9, 6, 5, 10]
Share the Github link to your solution.
"""
def reverseArray(A):
  
  #take the last item
  #take the firstitem 
  #swap
  """
  if the lenth of  the 
  array is even the Prog'
  will swap length/2
  if odd it will swap length//2
  """
  #CHECK THE LEN DIVIDE BY 2
  length=len(A)//2
  rev=-1
  revlen=-(length)
  """
  revlen is the length 
  that is used to accessed
  the items from the end of the list

  swap the last item with the first 
  item ,then move to the second item 
  with the second last item 

  the time complexity is O(n)
  """
  for i in range(length):
    if i!=0:  
      #if i is not 0 rev in incresed 
      rev=rev-1#since it is a negative value
    #make a swap   
    A[i],A[rev]=A[rev],A[i]
    #if we reach the last item 
    #break from the loop
    #rev is our counter from the last item 
    if rev==revlen:
      break#move out of the loop 
  print(A)#print the reversed array 


A=[10,5,6,9,7]
reverseArray(A)
