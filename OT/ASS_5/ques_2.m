clear all
clc
format short
variables = {'x_1','x_2','x_3','A_1','A_2','Solution'};
OVariables ={'x_1','x_2','x_3','Solution'};
OriginalCost = [-1 2 3 -1 -1 0];
info = [-2 1 3 1 0 2; 2 3 4 0 1 1];
BV = [4 5];
% fprintf('*********************** Phase 1************************\n');
cost = [0 0 0 -1 -1 0];       % Max z'=-a1-a2
A = info
StartBV=find(cost<0)
[BFS , A]= simp_max(A,StartBV,cost,variables)