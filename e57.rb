# http://projecteuler.net/index.php?section=problems&id=57
class Fraction
  attr_accessor :numerator, :denominator
  def initialize(n,d)
    @numerator = n
    @denominator = d
  end
  def display
    puts "#{@numerator} / #{@denominator}"
  end
  def add b
    if @denominator == b.denominator
      return Fraction.new(@numerator+b.numerator,@denominator)
    elsif @denominator == 1
      return Fraction.new(@numerator * b.denominator + b.numerator,b.denominator)
    end
  end
  def reciprocal
    @denominator,@numerator = @numerator,@denominator
    self
  end
  def exceeds?
    @numerator.to_s.size > @denominator.to_s.size
  end
end

_1 = Fraction.new(1,1)
_2 = Fraction.new(2,1)
num = Fraction.new(1,2)
count = 0
999.times {
  num = _2.add num
  num.reciprocal
  count += 1 if (_1.add num).exceeds?
}
p count