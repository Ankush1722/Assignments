%% Phase 1: Input parameter
C=[3 5]
A=[1 2; 1 1; 0 1]     % Constraints coefficents
B=[20; 15; 6]        % RHS of constraints

%% Phase 2: Identify <= or >= types constraints
Inequsign=[0 0 1]

%% Phase 3: Introduce the slag and surplus variable
s=eye(size(A,1));   % To generate identity matrix
index=find(Inequsign>0);
s(index,:)=-s(index,:)

%% Phase 4: Write the standard form
Object_funct=array2table(C);    % for representing the Objective Function
Object_funct.Properties.VariableNames(1:size(C,2))={'x1','x2'};

%represention of Constraints
Mat=[A s B]
constraint=array2table(Mat);
constraint.Properties.VariableNames(1:size(Mat,2))={'x1','x2','s1','s2','s3','B'};
Object_funct
constraint


















