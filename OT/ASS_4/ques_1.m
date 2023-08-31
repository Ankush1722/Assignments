%% To obatin BSF and then find the optimal solution.
%% Phase 1: Input paramenters
c = [2 3 4 7];
a = [2 3 -1 4; 1 -2  6 -7];  % Constrants coefficient
b = [8; -3];  % RHS of the constraints

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
        y = zeros(n,1);
        x = a(:,t(i,:))\b;

        if all(x>=0 & x~=inf & x~=-inf)
            y(t(i,:)) = x;
            sol = [sol y];
        end
    end
else
        error('Equation is larger variable')
end
sol

z=c*sol
[zmax, zindex] = max(z)


bfs=sol(:,zindex)
optimal_value=[bfs' zmax];

optimal_bfs=array2table(optimal_value);

optimal_bfs.Properties.VariableNames(1:size(optimal_bfs,2))={'x1','x2','x3','x4','z'}


























