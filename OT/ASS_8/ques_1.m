clc
clear all
format short
%% INPUT PARAMETER
Cost=[5 2 4 3;6 4 9 5;2 3 8 1]; %Cost of transportation Function
A=[30 40 55]; %Supply
B=[15 20 40 50];
%% TO CHECK UNBALANCED/BALANCED PROBLEM
if sum(A)==sum(B)
    fprintf("Given Transportation Problem is Balanced\n")
else
    fprintf("Given Transportation problem is Unbalanced\n")
    if sum(A)<sum(B)
        Cost(end+1,:)=zeros(1,size(B,2))
        A(end+1)=sum(B)-sum(A);
        B
    else
        Cost(:,end+1)=zeros(1,size(B,1))
        B(end+1)=sum(A)-sum(B)
        A
    end
end
ICost=Cost
X=zeros(size(Cost)); %Initial allocation
[m,n]=size(Cost);    %Finding the number of rows and columns
BFS=m+n-1;           %Total number of BFS
%% FINDING THE CELL (WITH MINIMUM COST) FOR THE ALL0CATION
for i=1:size(Cost,1)
    for j=1:size(Cost,2)

hh=min(Cost(:)); %For finding minimum cost value
[Row_Index,Col_Index]=find(hh==Cost); %Finding the position of minimum cost value
x11=min(A(Row_Index),B(Col_Index))
[Value,Index]=max(x11);%For finding Maximum allocation
ii=Row_Index(Index); %Identify the row position of lowest cost(hh) and Highest allocation(x11)
jj=Col_Index(Index);%Identify the colum position of lowest cost(hh) and Highest allocation(x11)
%y11=min(A(ii),B(jj)) %For finding the value 
X(ii,jj)=Value
A(ii)=A(ii)-Value;  %Update the table (Supply)
B(jj)=B(jj)-Value;  %Update the table (Requirement)
Cost(ii,jj)=Inf;    %Make the position where allocation is given to infinity so that it doesnt get into other iterations
    end
end
%% PRINT THE INITIAL BFS
fprintf('Initial BFS=\n')
IBFS=array2table(X);
disp(IBFS)
%% TO CHECK FOR DEGENERATE AND NON-DEGENERATE SOLUTION
TotaBFS=length(nonzeros(X));
if TotaBFS==BFS
    fprintf('The Initial BFS is Non-Degenerate \n');
else
    fprintf('The initial BFS is Degenerate');
end
%% TO COMPUTE THE INITIAL TRANSPORTATION COST
TransportationCost=sum(sum(ICost.*X))





















