

total = 1

# need to figure out how to check if even the add to total. 
# right now total is out of scope so we need to figure out 
# a wat to increment total.
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
   
print(recur_fibo(11))