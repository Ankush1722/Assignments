%%2
% Max Z= 5x1+18x2
% s.t. x1+2x2<=200
%      x1+x2<=150
%      0x1+x2<=60
%      x1,x2>=0
clear all

format short
%%Phase 1: Input the parameters
C=[5 8]; %Cost of objective function
A=[1 2;1 1;0 1]; %Constraint Coeff. matrix
B=[200;150;60]; %R.H.S. of constraint

%%Phase 2: Plotting the graph
x1=0:1:max(B);
x21=(B(1)-A(1,1).*x1)./A(1,2);
x22=(B(2)-A(2,1).*x1)./A(2,2);
x23=(B(3)-A(3,1).*x1)./A(3,2);
x21=max(0,x21);
x22=max(0,x22);
x23=max(0,x23);
plot(x1,x21,'r',x1,x22,'b',x1,x23,'g','linewidth',2)
xlabel('Value of x1');
ylabel('Value of x2');
title('x1 vs x2');
legend('x1+2x2\leq 200', 'x1+x2\leq 150','x2\leq 60');

%%Phase 3: Find corner points with areas
cx1=find(x1==0); %Points with x1 axis
c1=find(x21==0); %Points with x2 axis
Line1=[x1(:,[c1 cx1]); x21(:,[c1 cx1])]';
c2=find(x22==0);
Line2=[x1(:,[c2 cx1]); x22(:,[c2 cx1])]';
c3=find(x23==0)
Line3=[x1(:,[c3 cx1]); x23(:,[c3 cx1])]';
corpt=unique([Line1; Line2; Line3], 'rows')

%%Phase 4: Point of intersection 
RKR=[0;0];
 for i=1:size(A,1)
     A1=A(i,:);
     B1=B(i,:);
     for j=i+1:size(A,1)
         A2=A(j,:);
         B2=B(j,:);
         A3=[A1;A2];
         B3=[B1;B2];
         Xx=A3\B3; % or X=inv(A3)*B3, both will work
         RKR=[RKR Xx];
     end 
 end
 pt=RKR'
 
 %%Phase 5: Write all corner points
 allpoint=[pt;corpt];
 points=unique(allpoint, 'rows')
 
 %%Phase 6: Find the feasible region
 PT=constraints_2(points); %calling constraint function file
 PT=unique(PT,'rows')
 
 %%Phase 7: Compute the objective function
 for i=1:size(PT,1)
     fx(i,:)=sum(PT(i,:).*C);
 end
 vert_Funs=[PT,fx];
 
 %%Phase 8: Find the optimal value
 [fxval, indexfx]=max(fx);
 optval=vert_Funs(indexfx,:);
 OPTIMAL_BFS=array2table(optval)