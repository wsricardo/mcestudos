def fat(num):
     n = 1
     k = num
     if num==1:
             return 1
     elif num > 1:
             while k >= 1:
                     n = n*k
                     k -= 1
             return n
