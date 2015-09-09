function [P, GTS] = incrProd(P,B,GTS,newTrans)
%Function to incrementally update GTS and product automaton with new
%transitions
%
%Input should be product P, buchi B, game transition system GTS, and new
%transitions newTrans
%
%Written by Kevin Leahy March 2015

numTrans = size(newTrans,1); %number of transitions

ii = [];
jj = [];

for i = 1:numTrans %add each new transition incrementally
    
    %adding transitions to GTS
    source = double(newTrans{i}{1});
    dest = double(newTrans{i}{2});
    if source == 1151
        pause(0.1)
    end
    if dest == 1151
        pause(0.1)
    end
    %     source = find(ismember(GTS.Qp,squeeze(newTrans(i,1,:))','rows'));%source in GTS
    %     dest = find(ismember(GTS.Qp,squeeze(newTrans(i,2,:))','rows'));%dest in GTS
    GTS.adj(source,dest) = 1;%add trans to GTS
    
    %adding transitions to P
    Beta_PG = P.S(P.S(:,1)==source,2); %states in Buchi that are in product with source
    
    for j = 1:length(Beta_PG) %loop over state in Buchi, check for allowed trans, and add states to list
        
        sCurr = Beta_PG(j); %current state in buchi
        PCurr = find(ismember(P.S,[source sCurr],'rows')); %current state in product
        tr_s=find(~cellfun('isempty',B.trans(sCurr,:))); %indices (states) of B in which s_i can transit (for some predicates(observables))
        
        % AU: Blocking state fix
        if(isempty(tr_s))
            continue;
        end
        
        % Cell array holding propositions that enable transitions in the Buchi
        props = B.trans(sCurr,tr_s);
        
        % Which transitions can be actually taken?
        enabled = false(1,length(tr_s));
        pairs = [];
        
        for k = 1 : length(tr_s)
            % Check if we can goto tr_s(j) in buchi from this state
            if ismember(GTS.obs(source), props{k});
                pairs = [pairs; dest tr_s(k)];
            end
        end
        
        if(isempty(pairs))
            continue;
        end
        
        stateMask = ismember(P.S,pairs,'rows');
        targetStates = find(stateMask);
        % Row (source state)
        ii = [ii; PCurr*ones(length(targetStates),1)];
        % Column (target state)
        jj = [jj; targetStates];
        
    end
end

for i = 1:length(ii)
    P.trans(ii(i),jj(i)) = 1;
end

end

