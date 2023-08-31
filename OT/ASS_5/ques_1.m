 %% initialize
 C=[1 2];
 a=[-1 1;1 1];
 B=[1;2];
 S=eye(size(a,1));
 A=[a S B]
 Cost=[1 2 0 0 0];
 noofvariables =2;
 variables={'x_1','x_2','s_1','s_2','sol' };

 BV=(noofvariables+1):1:size(A,2)-1
 ZjCj=Cost(BV)*A-Cost
 ZCj=[ZjCj;A];
 
 SimplexTable = array2table(ZCj);
 SimplexTable.Properties.VariableNames(1:size(ZCj,2))=variables
 run=true;
 while run
    zc = ZjCj(1:end-1);
    if any(zc<0)
        fprintf('Sol is not optimal');
        fprintf('\n~~THE NEXT ITERATION~~\n');
        disp(' OLD BASIC VARIABLES');
        disp(BV);
        %Find entering variable
        [enter_var, pvt_col] = min(zc);
        fprintf('The most negative element is %d \n',enter_var);
        fprintf('Entering variable column is %d \n', pvt_col);
        % Find leaving variable
        if all(A(:, pvt_col)<=0)
            fprintf('LPP is unbounded\n')
        else
            sol = A(:, end);
            column = A(:, pvt_col);
            %finding min ratio
            for i = 1:size(column,1)
                if column(i)>0
                    ratio(i) = sol(i)/column(i)
                else
                    ratio(i) = inf
                end
            end
            [leaving_value,pvt_row] = min(ratio);
            fprintf('The min ratio is %d \n',leaving_value);
            fprintf('Leaving variable row is %d \n', pvt_row);
            pvt_key = A(pvt_row, pvt_col)
            BV(pvt_row)=pvt_col;
            A(pvt_row, :)=A(pvt_row,:)/pvt_key
            for i = 1:size(A,1)
                if i~=pvt_row
                    A(i,:) = A(i,:)-A(i, pvt_col)*A(pvt_row, :)
                end
            end
            ZjCj = Cost(BV)*A-Cost
            new_table = [ZjCj;A];
            array2table(new_table, 'VariableNames', variables)
        end
    else
        run = false;
    end
 end
 fprintf('The optimal sol is %f \n', ZjCj(end));