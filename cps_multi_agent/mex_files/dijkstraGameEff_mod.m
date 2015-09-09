function [dist] = dijkstraGameEff_mod(TM_old, F,turn)
%Modified dijkstra's algorithm for a game transition system
%
%Inputs are a transition matrix (can be sparse), destination node, and
%whose turn it is (1 is robot's turn, 0 is adversary's turn)
%
%Written by Kevin Leahy March 2015

TM = zeros([size(TM_old,1) size(TM_old,2)]+1);
TM(1:end-1,1:end-1) = TM_old;
% TM(end+1,:) = zeros(1,length(TM));%add row and column of zeros to add virtual end node
% TM(:,end+1) = zeros(length(TM),1);
TM(F,end) = 1; %add transitions to virtual node
n = length(TM);
dist = ones(n,1)*Inf;
dest = n; %make virtual node destination
dist(dest) = 0; %set dist to virtual node as 0
dist(F) = 0; %set dist to final states as 0
Q = 1:n-1; %consider all but final node
qInd = length(Q);
% Q = setdiff(Q,F); %remove final states from Q

% turnD = turn(dest); %is destination node robot turn?

while( qInd ~= 0) %begin dijkstra
    [val, qu] = min(dist(Q(1:qInd)));
    u = Q(qu); % index of the vertex
    if( isinf(dist(u) ))
        break;
    end
    Q(qu:end-1) = Q(qu+1:end);
    Q(end) = Inf;
    qInd = qInd-1;
    % Q = setdiff(Q, u);
    % all transitions to u TM(:,u);
    ind = (find(TM(:,u)==1))';
    for j=1:length(ind)
        i = ind(j);
        if turn(i) == 1 %robot's turn -- use regular dijkstra
            if dist(i) > (val + TM(i, u)) %&& (TM(i,u)~=0)
                dist(i) = val + TM(i, u);
            end
        else %environment's turn
            if ~isempty(find(TM(i,:)==1, 1)) && ~ismember(i,F)
                dist(i) = max(dist(TM(i,:)==1))+1; %maximum energy for next states
            end
        end
    end
end
% dist(dest) = 0; %manually make distance to this state 0
dist = dist(1:end-1);
% dist = dist - 1; %remove distance to virtual node, and keep distance to real nodes
end