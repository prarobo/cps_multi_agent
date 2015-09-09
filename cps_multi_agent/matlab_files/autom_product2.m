function P = autom_product2(T,B)
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
% sparse matrix to keep possible transitions (trans(i,j)=1 if S(i,:) can transit in S(j,:))
%trans=sparse(size(S,1),size(S,1));
ii = [];
jj = [];
ss = [];

for i=1:size(S,1) %search for possible transitions from current state (transitions enabled by T & B, as described in product of automata)
% for i=1:size(S,1) %search for possible transitions from current state (transitions enabled by T & B, as described in product of automata) 
    tr_q=find(T.adj(S(i,1),:));  %labels of states of T in which q_i can transit
    tr_s=find(~cellfun('isempty',B.trans(S(i,2),:))); %indices (states) of B in which s_i can transit (for some predicates(observables))
    
    % AU: Blocking state fix
    if(isempty(tr_s))
        continue;
    end
    
    if(isempty(tr_q))
        continue;
    end
    
    % Cell array holding propositions that enable transitions in the Buchi
    props = B.trans(S(i,2),tr_s);
    
    % Which transitions can be actually taken?
    enabled = false(length(tr_q),length(tr_s));
    pairs = [];
    for k = 1 : length(tr_q)
        for j = 1 : length(tr_s)
            % Check if we can goto tr_s(j) in buchi from this state
            if ismember(T.obs(S(i,1)), props{j});
               pairs = [pairs; tr_q(k) tr_s(j)]; 
            end
        end
    end
    
    if(isempty(pairs))
        continue;
    end

    stateMask = ismember(S,pairs,'rows');
    targetStates = find(stateMask);
    % Row (source state)
    ii = [ii; i*ones(length(targetStates),1)];
    % Column (target state)
    jj = [jj; targetStates];
    % Value (weight)
    ss = [ss; full(T.adj(S(i,1), S(stateMask, 1)))'];
end

P.trans = sparse(ii, jj, ss, length(T.Q)*length(B.S), length(T.Q)*length(B.S));
P.S = S;
P.S0 = S0;
P.F = F;
P.curr = P.S0;

