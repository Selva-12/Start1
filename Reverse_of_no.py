class Solution:
    def reverse(self, x: int) -> int:
  
          sign = 1

          if x < 0:
              sign =-1 # note if we directly try to multiply the sogn at the end the it will return 0

                         # as the below loop will only run if x >0. So to avoid that currently we are making it
              #to be +ve by mutlipying it with -1 and but making the sign as -1 so that later we can multiply it
              x*=-1 


          sums = 0   

          while x>0:
              rem = x%10
              sums= sums *10 +rem
              x//=10


          # checking if sums is within the range or not if not the return 0 
          if  not -2**31-1 <= sums<= 2**31:
              return 0

          return sums * sign
