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

num = Fraction.new(0,1)
(1..99).to_a.reverse.each {|i|
  num = Fraction.new((i+1)%3==0&&(i+1)/3*2||1,1).add num
  num.reciprocal
}

p (Fraction.new(2,1).add(num)).numerator.to_s.split(//).map{|i|i.to_i}.reduce(:+)