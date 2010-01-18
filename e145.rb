def reverse n
  curr = n
  result = 0
  while curr > 0
    result += curr%10
    result *= 10
    curr /= 10
  end
  result /= 10
end
def entirely_odd? n
  return false if n.even?
  curr = n
  while curr > 10
    return false if curr.even?
    curr /= 10
  end
  return true
end
#p entirely_odd? 131313
p (1..10**9).select { |e| e%10!=0  }.map { |e| e+reverse(e)  }.select { |e| entirely_odd? e}.size