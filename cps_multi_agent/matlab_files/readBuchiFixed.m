function B = readBuchiFixed(fileName,sizeAlph)
%Function to read ltl2ba results. Inputs are the name of the file with the
%output, and the number of propositions in the specification.
%
%Note: Care should be taken to inspect how ltl2ba assigns numbers to
%negated propositions
%
%Written by Kevin Leahy March 2015


baFile = fopen(fileName); %could add error check here if need be


tline = fgetl(baFile);
baString = tline;
tline = fgetl(baFile);
while ischar(tline)
    baString = [baString char(10) tline];
    tline = fgetl(baFile);
end

fclose(baFile);

Alph_s = alphabet_set(obtainAlphabet(sizeAlph)); %powerset alphabet, will go away with proper TS
B.alph = Alph_s;
r = baString;

sig=1:length(Alph_s);  %numeric labels for observables (integers)

str1=[char(10), 'Buchi automaton after simplification' char(10)];    %first string for match (char(10) - line feed)
str2=[char(10), 'never {'];    %second string for match (end of interesting "zone" from what ltl2ba returns)

%remove from beginning until line contained by str1 (including it), and
%from beginning of str2 to end
r_temp=r;
r([1:(findstr(r,str1)+length(str1)-1) , findstr(r,str2):end])=[];
if ~isempty(regexp(r,'empty automaton'))
    error('Empty Buchi automaton (maybe LTL formula has logical inconsistencies)');
end
if isempty(regexp(r_temp,'accept'))
    error('No accepting state in Buchi automaton (maybe LTL formula has logical inconsistencies)');
end

[S_names s_ind e_ind]=regexp(r, 'state (\S*)', 'tokens', 'start', 'end'); %S_names is a cell containing sub-cells with state names
%s_ind, e_ind contain start&end indices for expressions (useful for delimiting parts of r corresponding to a certain state)
S_names=[S_names{:}];   %get rid of sub-cells (S_names is a cell array of strings)
states_no=length(S_names);  %number of states in Buchi aut
B.S=1:states_no;    %numeric indices for states
B.S0=find( cellfun( 'isempty', regexp(S_names,'init') ) == 0 );    %find indices of state(s) containing word 'init' (initial st.)
B.F=find( cellfun( 'isempty', regexp(S_names,'accept') ) == 0 );    %find indices of state(s) containing word 'accept' (accepting states)

% If the init is accept, it will not show up in the state list
if ~isempty(findstr(r_temp,'accept_init'))
    B.F=[B.S0,B.F];
    if length(B.S0)>1
        error('Can not handle multiple init state where some are accepted yet, add this functionality!');
    end
    B.F=sort(B.F);
end

%find transitions (search succesors for each state and atomic proposition)
B.trans=cell(states_no,states_no);  %trans(i,k) gives the indices of elements from alphabet_set (with "or" between them) for which s_i -> s_k
for i=1:states_no
    if i~=states_no
        str=r((e_ind(i)+2): (s_ind(i+1)-1));   %select string containing transitions of current state (p1 -> . . .)
    else    %last state in string r
        str=r((e_ind(i)+2): end);
    end
    
    row=regexp(str,'([^\n]*)\n','tokens');  %token: ([^\n] - any character different than new line), (* - any number of such characters)
    row=[row{:}]; %cell with rows for current state (i) (each row contains one state)
    propList = sig;
    for j=1:length(row)
        % k=find( cellfun( 'isempty', regexp(row{j}, S_names) ) == 0 ); %index of state in which s_i transit (on current row)
        %k should be an integer (could be vector, if there are states like T0_S1, T0_S11, but this happens for unusually large formulas
        %in order to avoid this, use the following line (instead the above commented one):
        k=strmatch(row{j}((findstr(row{j},' -> ')+4) : end), S_names, 'exact'); %find string with state name and find index for exact matching in possible names
        
        %ONLY {& (and), ! (not), 1 (any=True)} can appear on each row with respect to propositions (|| (OR) operator results in 2 rows)
        %if 1 appears, it is the first element and there is no atomic
        %proposition on current row
        if row{j}(1)==num2str(1)
            B.trans{i,k}=sig;   %for all possible combinations of propositions there is transition s_i -> s_k
            continue
        end
        
        %1 does not appear on current row
        prop=row{j}(1 : (findstr(row{j},' -> ')-1)); %delimitate proposition (expression) involving atomic propositions
        %prop is only of kind "[!]pi & [!]pj & [!]pk" ([!] - ! appears or not)
        
        %OTHER TEMP FIX!
        prop=regexprep(prop,'{2}','!p3');
        prop=regexprep(prop,'{0}','!p1');
        prop=regexprep(prop,'{1}','!p2');
        prop=regexprep(prop,'{1,2}','!p2&!p3');
        
        atom_pr=regexp(prop,'([!p]+\d+)','tokens'); %separate in atomic propositions (possibly preceded by !)
        atom_pr=[atom_pr{:}];
        
        %TEMPORARY FIX!! NEED TO FIND OUT HOW LTL2BA ASSIGNS NEGATED PROPS
        %TO NUMBERS - KL 3/2/2015
%         if isempty(atom_pr)
%             atom_pr=regexp(prop,'(\d)','tokens');
%             atom_pr=[atom_pr{:}];
%             atom_pr=regexprep(atom_pr,'0','!p3');
%             atom_pr=regexprep(atom_pr,'1','!p2');
%             atom_pr=regexprep(atom_pr,'2','!p1');
            if isempty(atom_pr)
                continue
            end
%         end
        
        
        labels=sig;  %will store labels of elements of alphabet_set that enable current transition (respecting expression)
        %start with labels for whole alphabet_set, because we'll use intersections when updating vector "labels"
        for ap=1:length(atom_pr) %for each atomic prop, modify vector "labels"
            if isempty(findstr(atom_pr{ap},'!'))   %current atomic prop is not negated, so we keep ALL subsets that contain it,
                %not only the subset equal with current atomic proposition
                %use intersections because atomic propositions (possibly negated) are linked only by & (AND) operator
                labels=intersect(labels, find( cellfun( 'isempty', regexp(Alph_s,atom_pr{ap}) ) == 0 ));    %indices of subsets including current atomic prop.
            else    %negated, find all subsets that does NOT contain the current atomic proposition
                labels=intersect(labels, find( cellfun( 'isempty', regexp(Alph_s,atom_pr{ap}(2:end)) ) ~= 0 )); %add indices of all other subsets
            end
        end
        
        B.trans{i,k}=union(B.trans{i,k},labels);    %add current labels to current transitions (transition s_i -> s_k can be captured by more rows
        %(equivalent with OR operator between propositions)
    end
end
end