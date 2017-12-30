

import math
AB=int(input())
BC=int(input())
θrad = math.atan(AB/BC) 
θdeg =  θrad*57.2958
θ = round(θdeg)
print(str(θ)+'\N{DEGREE SIGN}')
