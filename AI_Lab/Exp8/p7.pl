% Facts
woman(jia).
man(john).
healthy(john).
healthy(jia).
wealthy(john).

% Rules
traveler(X):-healthy(X), wealthy(X).
travel(X):-traveler(X).
