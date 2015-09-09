function [ policy ] = gameUpdateInteg(wsDir, pyStates, numAgents, varargin)
%GAMEINTEG Incremental updates and getting control policy from the game inputs
%
%pyNewTrans should be the third input, which can be omitted if there is no
%new transition observed

updatePolicy = 0; %will be set to 1 if update is necessary for policy

%% Loading mat files
%load('newTrans.mat') %sample of 2 new transitions
load(sprintf('%s/gameVar.mat',wsDir)); %loading previously saved GTS

%Converting inputs
states = matConverter(pyStates, 'states', numAgents);

save(sprintf('%s/gameUpdateIntegMat.mat', wsDir));

%% Add new transitions if necessary
if nargin == 4
	pyNewTrans = varargin{1};
%     newTrans = matConverter(pyNewTrans, 'trans');
    newTrans = pyNewTrans';
    [P, GTS] = incrProd(P,Buchi,GTS,newTrans);
    %currently, no solution for updating energy function efficiently, so we can
    %call findEnergyGame again to update it for now
    [P.dist, P.Fstar] = findEnergyGame_mod_mex(full(P.trans),P.F,P.S,P.turn); %get distance to acceptance, Fstar
    updatePolicy = 1;
end

%% Updating current states
Bstate = P.S(P.curr,2); %get current Buchi state
[P, GTS] = updateStatesMulti(P,GTS,states,numAgents); %update states every time

if P.S(P.curr,2) ~= Bstate %state in Buchi has changed--need to update policy
    updatePolicy = 1;
end

%% Updating policy if necessary
if updatePolicy == 1
    policy = makePolicyMulti(P,GTS); %make policy
else
	policy = struct;
end

%% Saving workspace parameters
save(sprintf('%s/gameVar.mat', wsDir),'P','Buchi','GTS');
save(sprintf('%s/policy.mat', wsDir), 'policy'); %save policy as mat file
