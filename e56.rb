p (1..100).map{|a|(1..100).map{|b|(a**b).to_s.split(//).map{|e|e.to_i}.reduce(:+)}.max}.max