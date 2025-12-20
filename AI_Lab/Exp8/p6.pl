% Facts
cat(tom).
lovestoeat(kunal, pasta). 
lovestoplay(nawaz,games). 
hair(black).
lazy(patyusha).
happy(lily).
hungry(tom).
friends(jack, bili). 
play(ryan).

% Rules
dances (lili):-happy(lili).
searching(tom, food):-hungry(tom).
loves(jack, cricket), loves(bili, cricket):-friends(jack, bili). 
school(closed), free(ryan):-play (ryan).