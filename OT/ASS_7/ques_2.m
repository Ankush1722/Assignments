clc;
clear all;
%% INPUT PARAMETERS
Variables={'x1','x2','x3','s1','s2','Sol'};
Cost=[-2 0 -1 0 0 0];
info=[-1 -1 1 ;-1 2 -4 ];
B=[-5;-8];
s=eye(size(info,1));
A=[info s B]
% Find the starting BFS
BV=[];
for j=1:size(s,2)
    for i=1:size(A,2)
        if A(:,i)==s(:,j)
            BV=[BV i];
        end
    end
end
BV
disp(Variables(BV))
% Computer Z-roq(Zj-Cj)
ZjCj=Cost(BV)*A -Cost;
% Print the table
ZCj=[ZjCj;A];
simptable=array2table(ZCj);
simptable.Properties.VariableNames(1:size(ZCj,2))=Variables

%% DUAL SIMPLEX METHOD 
Run=true;
while Run

sol=A(:,end)
if any(sol<0)
    fprintf('The current BFS is not Feasible\n\n');
    % Finding the Leaving Variable
    [leavingVal, PvtRow]=min(sol);
    fprintf('Leaving Row=%d',PvtRow)
    
    % Finding the entering variable
    Row=A(PvtRow,1:end-1);
    ZRow=ZjCj(1,1:end-1);

    for i=1:size(Row,2)
        if Row(i)<=0
            ratio(i)=abs(ZRow(i)./Row(i));
        else
            ratio(i)=inf;
        end
    end
    % Finding the minimum ratio
    [MinRatio,PvtCol]=min(ratio);
    fprintf('Entering variable is %d\n\n',PvtCol)
    BV(PvtRow)=PvtCol;
    fprintf('Basic Variable (BV)=')
    disp(Variables(BV))

    %PvtKey
    PvtKey=A(PvtRow,PvtCol);
    %Update the Table for next iteration
    A(PvtRow,:)=A(PvtRow,:)./PvtKey;
    for i=1:size(A,1)
        if i~=PvtRow
            A(i,:)=A(i,:)-A(i,PvtCol).*A(PvtRow,:);
        end
    ZjCj=ZjCj-ZjCj(PvtCol).*A(PvtRow,:);
    end

    ZCj=[ZjCj;A];
    simptable=array2table(ZCj);
    simptable.Properties.VariableNames(1:size(ZCj,2))=Variables
else
    Run=false;
    fprintf('The current BFS is Feasible and Optimal\n');
end
end

% Final Optimal Solution
FinalBFS=zeros(1,size(A,2));
FinalBFS(BV)=A(:,end);
FinalBFS(end)=sum(FinalBFS.*Cost);
OptimalBFS= array2table(FinalBFS);
OptimalBFS.Properties.VariableNames(1:size(OptimalBFS,2))=Variables


























