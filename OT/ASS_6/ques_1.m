clc
clear all
format short
%% INPUT PARAMETER
Variables = {'x1','x2','s1','s2','a1','a2','sol'};
M = 1000;
% Cost of LPP
Cost = [ -2 -1 0 0 -M -M 0]; 
% Constraints
A = [ 3 1 0 0 1 0 3; 4 3 -1 0 0 1 6; 1 2 0 1 0 0 3]; 
s = eye(size(A,1));
%% FINDING THE STARTING BFS BASIC VARIABLES
BV = [];
for j=1:size(s,2)
   for i = 1:size(A,2)
        if A(:,i)==s(:,j)
            BV = [BV i]; 
        end   
   end
end
BV
%% TO COMPUTE THE Z-ROW (Zj-Cj)
ZjCj = Cost(BV)*A-Cost;
ZCj = [ZjCj; A];
Simplextable = array2table(ZCj);
Simplextable.Properties.VariableNames(1:size(ZCj,2)) = Variables
%% SIMPLEX METHOD STARTS
run = true;
while run
    ZC = ZjCj(:,1:end-1);
    if any(ZC<0)      % check any negative value
        fprintf('Current BFS is not optimal\n');
        fprintf('Next iteration is required\n');
        
        % find the entering variable
        [Entval,pvt_col] = min(ZC);
        fprintf('Entering Column is %d \n', pvt_col);
        
        % find leaving variable
        sol = A(:,end);
        Column = A(:,pvt_col);
        if all(Column<=0)
            error('LPP has unbounded solution')
        else
           % check minimum ratio with positive entries 
           for i = 1:size(Column,1)
               if Column(i)>0
                ratio(i) = sol(i)./Column(i);
               else
                   ratio(i) = inf;
               end
           end
        
           % to find the minimum  ratio
           [MinRatio, pvt_row] = min(ratio);
           fprintf('The leaving row is %d \n',pvt_row);
        end
        BV(pvt_row) = pvt_col;
        pvt_key = A(pvt_row,pvt_col);
        % Update the table for next iteration
        A(pvt_row,:)=A(pvt_row,:)./pvt_key;
        for i=1:size(A,1)
            if i~=pvt_row 
                A(i,:) = A(i,:) - A(i,pvt_col).*A(pvt_row,:);
            end
        end
        ZjCj =ZjCj-ZjCj(pvt_col).*A(pvt_row,:);
        ZCj = [ZjCj;A];
        SimpTable = array2table(ZCj);
        SimpTable.Properties.VariableNames(1:size(ZCj,2))= Variables
    else
        run=false;
        fprintf('Current BFS is optimal\n');
        fprintf('Phase End');
        BFS=BV;
    end
end
BFS = zeros(1,size(A,2));
BFS(BV) = A(:,end);
BFS(end) = sum(BFS.*Cost);
currentBFS = array2table(BFS);
currentBFS.Properties.VariableNames(1:size(currentBFS,2)) = Variables












