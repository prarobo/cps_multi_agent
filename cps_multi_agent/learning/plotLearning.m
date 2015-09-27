%% Initialize
clc; clearvars; close all;

%% Loading learning data
load('adv_learning_results.mat');
numPolicyFactors = 77;

%% Getting trial length
numFactorList = cellfun(@double, numFactorList, 'UniformOutput', false);
numRuns = length(numFactorList);
trialLen = cellfun(@length, numFactorList);
plotTrialLen = roundn(max(trialLen),1);

%% Plot matrix form
plotTrialData = zeros(plotTrialLen, numRuns);
for i=1:numRuns
    plotTrialData(1:length(numFactorList{i}),i) = numFactorList{i};
    
    if plotTrialLen >= length(numFactorList{i})+1
        plotTrialData(length(numFactorList{i})+1:end,i) = numFactorList{i}(length(numFactorList{i}));
    end
end

%% Policy distance
policyDistance = numPolicyFactors-plotTrialData;

plot(policyDistance, 'LineWidth', 2)
hold on
plot(1:plotTrialLen, mean(policyDistance,2), 'k','LineWidth', 4)

xlabel('Number of moves', 'FontSize', 30)
ylabel('Policy distance D_{pd}', 'FontSize', 30)
xt = get(gca, 'XTick');
set(gca, 'FontSize', 24)
yt = get(gca, 'YTick');
set(gca, 'FontSize', 24)

