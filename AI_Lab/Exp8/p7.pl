woman(jia).
man(john).
healthy(john).
healthy(jia).
wealthy(john).

traveler(X):-healthy(X), wealthy(X).
travel(X):-traveler(X).