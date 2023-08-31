%% To obatin BSF and then find the optimal solution.
%% Phase 1: Input paramenters
c = [-1 2 -1];          
a = [-1 1 0; -1 0 2];  % Constraint coefficients
b = [6; 4];  % RHS of the constraints

%% Phase 2: No of constraints and variables
m = size(a,1)
n = size(a,2)

%% Phase 3: Compute the ncm BFS
nab = nchoosek(n,m)  % No. of possible basic solutions
t = nchoosek(1:n,m)  % Pair of basic solution

%% Phase 4: Constrtuct the basic solution
sol = [];  % Default solution is zero

if n >= m
    for i = 1 : nab
        y = zeros(n,1);       %stores the calculated value of variables
        x = a(:,t(i,:))\b;    %calculated value of current basic variables
       
% Check the feasibility condition for current basic variables
        if all(x>=0 & x~=inf & x~=-inf)          %constarints of all variables
                y(t(i,:)) = x;                   %updates the value of current basic variables
                if any(t(i,:)==1 | t(i,:)==2)    %check constraints of x1 and x2
                        if(y(1)>4 |y(2)>4)
                            y=[];
                        end
                end
                sol = [sol y];   %a basic feasible solution is added to the solution matrix
        end
    end
else
        error('No. of variables less than no. of equations: infinite solutions')
end
sol

if(~(isempty(sol)))
    z=c*sol     %matrix multiplication to obtain BFS
    [zmax, zindex] = max(z)
    bfs=sol(:,zindex)
    optimal_value=[bfs' zmax];

    optimal_bfs=array2table(optimal_value);

    optimal_bfs.Properties.VariableNames(1:size(optimal_bfs,2))={'x1','x2','x3','z'}
else
    error('No possible solution')
end