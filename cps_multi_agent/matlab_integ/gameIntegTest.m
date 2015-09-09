% function [ policy ] = gameInteg(pyGameAlphabet, pyGameStates, pyGameTrans, pyGameStateLabels, pyGameInitState, numAgents)
%GAMEINTEG Getting control policy from the game inputs

%% Loading .mat
% load('gameAlphabet.mat')
% load('gameStates.mat')
% load('gameTransitions.mat')
% load('gameStateLabels.mat')

%% Converting python inputs
gameAlphabet = matConverter(pyGameAlphabet, 'alph', numAgents);
gameStates = matConverter(pyGameStates, 'states', numAgents);
% gameTrans = matConverter(pyGameTrans, 'trans', numAgents);
gameTrans = pyGameTrans';
gameStateLabels = matConverter(pyGameStateLabels, 'labels', numAgents);
gameInitState = matConverter(pyGameInitState, 'states', numAgents);

% save(sprintf('%s/gameIntegMat.mat', wsDir));

%% GTS computation
GTS = loadGameMulti(gameStates,gameTrans,gameStateLabels, gameInitState); %make GTS
Buchi = readBuchiFixed('SurvAvoid.txt',3); %read Buchi

P = autom_product_eff(GTS,Buchi,gameTrans); %make product

P.turn = zeros(size(P.S,1),1);
for i = 1:size(P.S,1) %loop to find whose turn for the product
   P.turn(i) = GTS.turn(P.S(i,1));
end

[P.dist, P.Fstar] = findEnergyGame_mod(P.trans,P.F,P.S,P.turn); %get distance to acceptance, Fstar 

policy = makePolicyMulti(P,GTS); %make policy
% policy = 0

%% Saving workspace parameters
%save(sprintf('%s/gameVar.mat', wsDir),'P','Buchi','GTS');
%save(sprintf('%s/policy.mat', wsDir), 'policy');


