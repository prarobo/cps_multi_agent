function [ policy ] = makePolicyMulti(P,T)
%This function uses the energy function for a product automaton to generate
%a control policy for an agent in a transition system
%
%Inputs are P, a product automaton, and T, a transition system
%
%Written by Kevin Leahy 04-APR-2015

stratStates = P.S(P.turn~=0,:);
% policy = [];

BState = P.S(P.curr,2); %current state in Buchi

for i = 1:length(stratStates)
    %make tuples of GTS state, buchi state, and next GTS state
    currQ = T.Qp(stratStates(i,1),:); %current GTS state
    currB = stratStates(i,2); %current Buchi state
    currS = find(ismember(P.S,stratStates(i,:),'rows')); %prod state index
    currV = P.dist(currS);
    if currB == BState %update only if state is current buchi state
        if P.dist(currS) == Inf
            eval(sprintf('policy.%s = 0;',currQ));
        else
            next = find(P.trans(currS,:)==1);
            if ~isempty(next)
                dist = P.dist(next);
                mu = next(find(dist==min(dist)));
                mu = T.Qp(P.S(mu(1),1),:);
                eval(sprintf('policy.%s = ''%s'';',currQ,mu));
            else
                eval(sprintf('policy.%s = 0;',currQ));
            end
        end
    end
end

end
