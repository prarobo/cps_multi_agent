function [GTS] = loadGameSparse_NewLabels(states,trans,labels,Q0)
%This is a function to take outputs from the game transition system
%generated by the python code and turn it into a matlab object. The states,
%alphabet, and transitions should already be loaded as character matrices
%in MATLAB
%
%Currently, the location of labels is hard-coded, but we can add
%flexibility to read this information from Python
%
%Written by Kevin Leahy March 2015

ii = []; %initialize vars for sparse transition matrix
jj = [];
ss = [];
GTS.Q = states;
n = size(GTS.Q,1);

for i = 1:size(trans,1)
    
    S1=double(trans{i}{1});
    S2=double(trans{i}{2});
    ii = [ii; S1]; %source node
    jj = [jj; S2]; %destination node
    ss = [ss; 1];  %transition weight
    
end

GTS.adj = sparse(ii,jj,ss,length(states),length(states)); %sparse transition matrix

alph = alphabet_set(obtainAlphabet(3)); %get alphabet
%visit p1 and p2 inf often, eventually p3
GTS.labels = cell(n,1); %initialize labels
GTS.obs = ones(n,1)*find(strcmpi('p4',alph)==1); %initialize obs numbers
GTS.turn = zeros(n,1);

for i = 1:n %loop over states

    props = eval(sprintf('labels.%s',GTS.Q(i,:)));
    propQ = [];
    if(~isempty(props.p1))
        propQ = strcat(propQ,'p1');
    end
    if(~isempty(props.p2))
        propQ = strcat(propQ,'p2');
    end
    if(~isempty(props.p3))
        propQ = strcat(propQ,'p3');
    end
    if isempty(propQ)
        propQ = 'p4';
    end
    
    GTS.labels{i} = propQ;
    GTS.obs(i) = find(strcmpi(propQ,alph)==1);
    
    if GTS.Q(i,end-1) == 'R'
        GTS.turn(i) = GTS.Q(i,end)+1;%add 1 to robot number for whose turn it is
    end

end

GTS.Qp = GTS.Q; %set Q prime equal to Q (words)
GTS.Q0 = find(ismember(GTS.Qp,Q0,'rows'));

GTS.Q = 1:n;
GTS.curr = GTS.Q0;

end