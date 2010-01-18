def find(k)
  sqrt(1+8*k*(k-1))%2 == 1
end
#2*k*(k-1) = n*n+n
#1+8*k*(k-1) = (2n+1)**2

def find_(k)
	return (1+8*k*(k-1))**0.5/2+0.5#-2*k*(k-1)
end

k = (1000000000000/(2**0.5)).to_i
p k
until find(k) do
   #p find_ k
   k += 1
end
p k
#p find_(707106781839)
#print ((1000000000000**2)*0.5)