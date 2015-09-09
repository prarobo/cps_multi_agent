function [P,GTS] = updateStatesMulti(P,GTS,states,numAgents)
%This function updates the current states of the product automaton and game
%transition system based on states that are fed in from python.
%
%Written by Kevin Leahy April 2015

% load('states.mat'); %read in previous state and current state

%% Find states in GTS
for i = 1:numAgents+1 %need +1 to account for adversary
state(i) = find(ismember(GTS.Qp,states(i,:),'rows'));
end

GTS.curr = state(numAgents+1); %upate current state in GTS

%% Update current state in GTS and P
for i = 1:numAgents+1 %loop over last state and current state
    
    possIndex = find(P.trans(P.curr,:)==1); %indices of possible next states
    possStates = P.S(possIndex,:); %possible next states
    P.curr = possIndex(find(possStates(:,1)==state(i))); %update current state in P
    if isempty(P.curr) %no current state -- indicates that violation of spec has occurred
        P.curr = find(ismember(P.S,[GTS.curr,P.S(P.S0,2)],'rows'));%reset Buchi state if we've reached bad state
    elseif length(P.curr) > 1 %multiple possible states -- prioritize final states
        inFstar = ismember(P.curr,P.Fstar); %check if in final states
        if sum(inFstar)>0 %at least one transition to final state
            P.curr = P.curr(inFstar);
            P.curr = P.curr(1); %in case more than one final (shouldn't be possible) take first final state
        else
            indCurr = find((P.S(P.curr,2))==max(P.S(P.curr,2))==1); %index of state with highest Buchi state
            P.curr = P.curr(indCurr);
        end
    end
end