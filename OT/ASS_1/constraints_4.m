function output=constraints(X)

%% Write 1st constraint

x1=X(:,1);
x2=X(:,2);
const1=20.*x1+50.*x2-480; % <sign\
h1=find(const1<0); % To violate the condition
X(h1,:)=[]; %delete by empty


%% Write 2nd constraint

x1=X(:,1);
x2=X(:,2);
const2=80.*x1+50.*x2-720; % <sign\
h2=find(const2<0); % To violate the condition
X(h2,:)=[]; %delete by empty

output=X;
end
