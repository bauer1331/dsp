'''Elvis Presley had a twin brother who died at birth. What is the probability 
that Elvis was an identical twin? Assume we observe the following probabilities
 in the population: fraternal twin is 1/125 and identical twin is 1/300. 



 P(brothers) = P(brothers|ident)*P(ident)+P(brothers|frat)*P(frat)
 P(brothers|ident) = 1/2
 P(brothers|frat) = 1/2*1/2 = 1/4
 P(frat) = 1/125
 P(ident) = 1/300

 P(ident|brothers) = (P(brothers|ident)P(ident))/P(brothers)
 P(ident|brothers) = (P(brothers|ident)P(ident))/P(brothers|ident)*P(ident)+P(brothers|frat)*P(frat)
 P(ident|brothers) = ((1/2)*(1/300))/((1/2)*(1/300)+(1/4)*(1/125))
 '''

p_ident = 1/300.0
p_frat = 1/125.0
p_bro_ident = 1/2.0
p_bro_frat = 1/4.0
p_brothers = p_bro_ident * p_ident + bro_frat * p_frat

p_ident_bro = (p_bro_ident*p_ident)/p_brothers