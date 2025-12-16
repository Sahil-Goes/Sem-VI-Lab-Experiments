% facts
dog(fido).
dog(rover).
dog(tom).

cat(mary).
cat(bill).

large(fido).
large(rover).
large(bill).

% rules
largeanimal(X) :- large(X), dog(X).
