%% Phase 1: Input parameter
C=[1 -3 2]
A=[3 -1 2; -2 4 0; -4 3 2]     % Constraints coefficents
B=[7; 2; 4]                   % RHS of constraintsS

%% Phase 2: Identify <= or >= types constraints
Inequsign=[0 0 1]

%% Phase 3: Introduce the slag and surplus variable
s=eye(size(A,1));   % To generate identity matrix
index=find(Inequsign>0);
s(index,:)=-s(index,:)

%% Phase 4: Write the standard form
Object_funct=array2table(C);    % for representing the Objective Function
Object_funct.Properties.VariableNames(1:size(C,2))={'x1','x2','x3'};

%represention of Constraints
Mat=[A s B]
constraint=array2table(Mat);
constraint.Properties.VariableNames(1:size(Mat,2))={'x1','x2','x3','s1','s2','s3','B'};
Object_funct
constraint
































