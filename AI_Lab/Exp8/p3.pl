% Facts
likes(john, mary).
likes(john, susie).
likes(X, susie).      % Everyone likes Susie
likes(john, X).       % John likes everybody
likes(X, john).       % Everybody likes John
dislikes(john, pizza).

% Rules
likes(john, susie) :- likes(john, mary).
