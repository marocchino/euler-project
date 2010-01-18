$p = Hash.new {|hash,k| hash[k] = k*(3*k-1)/2 }

(1..250).map { |e| p $p[e] }

