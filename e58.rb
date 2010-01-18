#[code {brush: java}][/code]
#[code {brush: bash}][/code]
# libprime.rb
# A much faster prime class.
# 
class Integer
  def isPrime?
    if self < 2
      return false
    elsif self < 4
      return true
    elsif self % 2 == 0
      return false
    elsif self < 9
      return true
    elsif self % 3 == 0
      return false
    else
      r = (self**0.5).floor
      f = 5
      f.step r,6 do |g|
        if self % g == 0
          return false
        end
        if self % (g + 2) == 0
          return false
        end
      end
      return true
    end
  end
end
diagonals = Hash.new { |hash, n| hash[n] = hash[n-2]+[n**2-3*(n-1),n**2-2*(n-1),n**2-n+1].select { |e|e.isPrime? }.size  }
diagonals[3] = 3
num = 3
while true
  num+=2
  break if (num-1)*2+1 > 10 * diagonals[num]
end
p num
