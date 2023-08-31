clear all
clc
format short
variables = {'x_1','x_2','s_1','s_2','A_1','A_2','Solution'};
OVariables ={'x_1','x_2','s_1','s_2','Solution'};
OriginalCost = [3 5 0 0 1 1 0];
info = [1 3 -1 0 1 0 3; 1 1 0 -1 0 1 2];
BV = [5 6];
% fprintf('*********************** Phase 1************************\n');
cost = [0 0 0 0 1 1 0];       % Min z'= a1+a2
A = info
StartBV=find(cost>0)
[BFS , A]= simp_min(A,StartBV,cost,variables)
%fprintf('************* Start of Phase 2 *************************\n')
A(:,StartBV)=[]; % remove artificial variables by giving them empty value
OriginalCost(:,StartBV)=[]; %Removing artificial Variables cost
[OptBFS , OptA]=simp_min(A, BFS , OriginalCost , OVariables)
Final_BFS=zeros(1,size(A,2));
Final_BFS(OptBFS)=OptA(:,end);
Final_BFS(end)=sum(Final_BFS.*OriginalCost)