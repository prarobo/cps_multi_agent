function [dist, FStar] = findEnergyGame(trans,F,S,turn)
%function takes transition relation, accepting states, and states and returns a vector
%of distance to acceptance

cF = size(F,2); %cardinality of F

d = dijkstraGameEff_mod(trans,F,turn); %call djikstra for each final state

FStar = F; %set FStar to F then prune

for i = 1:cF
    next = find(trans(F(i),:)==1);
    minD = min(d(next));
    if minD == Inf
        FStar = setdiff(FStar,F(i));
    end
end

dist = dijkstraGameEff_mod(trans,FStar,turn);

end

