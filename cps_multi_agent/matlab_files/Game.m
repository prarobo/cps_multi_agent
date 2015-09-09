%script to create game transitions system(from python output), buchi
%automaton (from ltl2ba output), and product automaton
%
%Written by Kevin Leahy March 2015

close all
clear all
clc

%load .mat files
load('gameAlphabet.mat')
load('gameStates.mat')
load('gameTransitions.mat')
load('gameStateLabels.mat')

GTS = loadGameSparse_NewLabels(gameStates,gameTrans,gameLabels); %make GTS
Buchi = readBuchiFixed('SurvAvoid.txt',3); %read Buchi
P = autom_product2(GTS,Buchi); %make product
P.turn = zeros(size(P.S,1),1);
for i = 1:size(P.S,1) %loop to find whose turn for the product
    P.turn(i) = GTS.turn(P.S(i,1));
end

[P.dist, P.Fstar] = findEnergyGame(P.trans,P.F,P.S,P.turn); %get distance to acceptance, Fstar 
policy = makePolicy(P,GTS); %make policy
save('policy.mat','policy') %save policy as mat file

%uncomment below for example of incremental construction of product

% load('newTrans.mat') %sample of 2 new transitions
% [P2, GTS2] = incrProd(P,Buchi,GTS,newTrans);
% 
% %currently, no solution for updating energy function efficiently, so we can
% %call findEnergyGame again to update it for now
% [P2.dist, P2.Fstar] = findEnergyGame(P2.trans,P2.F,P2.S,P2.turn); %get distance to acceptance, Fstar 
% policy = makePolicy(P2,GTS2); %make policy
% save('policy.mat','policy') %save policy as mat file
