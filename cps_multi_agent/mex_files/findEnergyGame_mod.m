function [dist, FStar] = findEnergyGame_mod(trans,F,S,turn)
%function takes transition relation, accepting states, and states and returns a vector
%of distance to acceptance

cF = size(F,2); %cardinality of F

d = dijkstraGameEff_mod(trans,F,turn); %call djikstra for each final state

FStar = F; %set FStar to F then prune
numInd = cF;

for i = 1:cF
    if(~isempty(d(trans(F(i),:)==1)))
        minD = min(d(trans(F(i),:)==1));
        if minD == Inf
            ind = ~(FStar(1:numInd)==F(i));
            numInd = sum(ind(:));
            FStar(1:numInd) = FStar(ind);
            FStar(numInd+1:end) = Inf;
            %FStar = setdiff(FStar,F(i));
        end
    end
end

dist = dijkstraGameEff_mod(trans,FStar(1:numInd),turn);

end

