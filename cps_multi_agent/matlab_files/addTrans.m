function GTS = addTrans(GTS,newTrans);
%function to add transition to GTS when newTransitions are received
%inputs are existing GTS and new transitions saved from python
%
%Written by Kevin Leahy March 2015

numTrans = size(newTrans,1); %number of new transitions

for i = 1:numTrans %loop over transitions to be added

    source = find(ismember(GTS.Qp,squeeze(newTrans(i,1,:))','rows')); %source node
    dest = find(ismember(GTS.Qp,squeeze(newTrans(i,2,:))','rows')); %destination
    GTS.adj(source,dest) = 1; %add to trans
    
end

end