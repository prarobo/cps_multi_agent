function [dist] = dijkstraGame(TM, dest,turn)
%Modified dijkstra's algorithm for a game transition system
%
%Inputs are a transition matrix (can be sparse), destination node, and
%whose turn it is (1 is robot's turn, 0 is adversary's turn)
%
%Written by Kevin Leahy March 2015


n = length(TM);
dist = ones(n,1)*Inf;

dist(dest) = 0;
Q = [1:n];

turnD = turn(dest); %is destination node robot turn?

while( ~isempty(Q) )
    [val, qu] = min(dist(Q));
    u = Q(qu); % index of the vertex
    if( isinf(dist(u) ))
        break;
    end
    Q = setdiff(Q, u);
    % all transitions to u TM(:,u);
    for i=1:n
        if turn(i) == 1 %robot's turn -- use regular dijkstra
            if( dist(i) > val + TM(i, u)) && (TM(i,u)~=0)
                dist(i) = val + TM(i, u);
            end
        else %environment's turn
            if ~isempty(find(TM(i,:)==1))
                dist(i) = max(dist(find(TM(i,:)==1))); %maximum energy for next states
            end
        end
    end
end
dist(dest) = 0; %manually make distance to this state 0
end