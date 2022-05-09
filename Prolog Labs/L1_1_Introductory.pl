/* Facts: 
1. Relationship Facts */

relationship(albert,alice).
relationship(bob,catherine).
relationship(john,juliet).

/* Facts: 
2. Rest related Facts */

restfull(albert).
restfull(john).

/* Facts: 
3. Parent related facts and geneology */
isParent(john,julian).
isParent(juliet,julian).
isParent(qiriakos,john).
isParent(sofi,john).
isParent(thanasis,juliet).
isParent(stavroula,juliet).

/* Rules (Axioms): 
1. One conditional Rules about happiness state */

happy(Male):-
	relationship(Male,Female).

/* Rules (Axioms): 
2. Two conditional Rule about ability to dance */
dances(Male) :-
	happy(Male),
	restfull(Male).
	
/* Rules (Axioms): 
3. Multi-Conditional Rule regarding display of all 4 grandparents of an atom*/
grandparent(Old_individual, Young_individual) :-
		isParent(Intermediate,Young_individual),
		isParent(Old_individual, Intermediate).




