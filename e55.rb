#[code {brush:ruby}]
def palindromic e
  (a=e.to_s)!=a.reverse
end
def gen e
  e+e.to_s.reverse.to_i
end
def filter e
  e.map{|e|gen e}.select{|e|palindromic e}
end

a = (1..10000).to_a
count = 0
while count < 3
  pre_size = a.size
  a = filter a
  count += 1 if (pre_size == a.size)
end
p a.size