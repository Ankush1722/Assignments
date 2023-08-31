%%4
% Min  Z = 40x1 + 24x2
% s.t. 20x1 + 50x2 ≥ 480,
%      80x1 + 50x2 ≥ 720,
%      x1, x2 ≥ 0
clear all

format short
%%Phase 1: Input the parameters
C=[40 24]; %Cost of objective function
A=[20 50;80 50]; %Constraint Coeff. matrix
B=[480;720]; %R.H.S. of constraint

%%Phase 2: Plotting the graph
x1=0:1:max(B);
x21=(B(1)-A(1,1).*x1)./A(1,2);
x22=(B(2)-A(2,1).*x1)./A(2,2);
x21=max(0,x21);
x22=max(0,x22);
plot(x1,x21,'r',x1,x22,'b','linewidth',2)
xlabel('Value of x1');
ylabel('Value of x2');
title('x1 vs x2');
legend('20x1+50x2\geq 480', '80x1+50x2\geq 720')

%%Phase 3: Find corner points with areas
cx1=find(x1==0); %Points with x1 axis
c1=find(x21==0); %Points with x2 axis
Line1=[x1(:,[c1 cx1]); x21(:,[c1 cx1])]';
c2=find(x22==0);
Line2=[x1(:,[c2 cx1]); x22(:,[c2 cx1])]';
corpt=unique([Line1; Line2], 'rows')

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
 PT=constraints_4(points); %calling constraint function file
 PT=unique(PT,'rows')
 
 %%Phase 7: Compute the objective function
 for i=1:size(PT,1)
     fx(i,:)=sum(PT(i,:).*C);
 end
 vert_Funs=[PT,fx];
 
 %%Phase 8: Find the optimal value
 [fxval, indexfx]=min(fx);
 optval=vert_Funs(indexfx,:);
 OPTIMAL_BFS=array2table(optval)
 
 
 