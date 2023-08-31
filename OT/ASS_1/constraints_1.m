function output=constraints(X)
%% Write 1st constraint

x1=X(:,1);
x2=X(:,2);
const1=2.*x1+x2-104; % <sign\
h1=find(const1>0); % To violate the condition
X(h1,:)=[]; %delete by empty


%% Write 2nd constraint

x1=X(:,1);
x2=X(:,2);
const2=x1+2.*x2-76; % <sign\
h2=find(const2>0); % To violate the condition
X(h2,:)=[]; %delete by empty

output=X;
end
