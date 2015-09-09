function P = autom_product_eff(T,B,gameTrans)
%performs the product of 2 finite automata
%first automaton (T) is in fact a finite transition system with observables
%(a state has ONLY one observable - a label from set of subsets of all possible observables - see alphabet_set & trasition system for sub-polytopes construction)
%second one (B) is one with guards on transitions (in this case a Buchi automata)
%a guard can be any combination of observables (as they would have "or" between them) - any subset of sets of alphabet_set
%(the alphabet of B (set of guards) is (must be) included (or equal) in the set of observations of T, given by alphabet_set)
%T and B are implemented as structures (see functions trans_sys_polytope and create_buchi, which construct T and B, respectivelly)

%T has fields Q, Q0, obs, adj (set of observables is 1:length(alphabet_set))
%If T.adj(i,j)=0, then there is no transition from i to j
%Otherwise, T.adj(i,j) is the weight on the transtion from i to j
%B has fields S, S0, F, trans
%P is the product automaton
%If there is a transition between (Ti,Sj) to (Tk,Sl), then
%P.adj((Ti,Sj),Tk,Sl))=T.adj(Ti,Tk) (i.e. the weights are inherited from
%the transition system

% States of product (row i gives on position 1 state from T, on position 2 state of B)
S=cartesian_product(T.Q,B.S);
% Initial and final states
S0=find(ismember(S(:,1)', T.Q0) & ismember(S(:,2)', B.S0));
F = find(ismember(S(:,2)', B.F));

P.S = S;
P.S0 = S0;
P.F = F;
P.curr = P.S0;

[rowB,colB] = size(B.trans);
numS = size(S,1);
%P.trans = sparse(numS,numS);
P.trans = false(numS,numS);

numT = size(gameTrans,1); %number of transitions
for i = 1:numT %loop over edges in TS
    labT = T.obs(gameTrans{i}{1});
    for j = 1:rowB %loop over edges in Buchi
        for k = 1:colB
            % if ismember(labT,B.trans{j,k}) %enables transition in Buchi
            if any(labT==B.trans{j,k}) %enables transition in Buchi
                %add edge from T1,B1 to T2,B2
                % source=find(ismember(S(:,1)', gameTrans{i}{1}) & ismember(S(:,2)', j));
                % dest=find(ismember(S(:,1)', gameTrans{i}{2}) & ismember(S(:,2)', k));
                source=(S(:,1)'== gameTrans{i}{1}) & (S(:,2)'== j);
                dest=(S(:,1)'== gameTrans{i}{2}) & (S(:,2)'== k);
                
                P.trans(source,dest) = 1;
            end
        end
    end
end


