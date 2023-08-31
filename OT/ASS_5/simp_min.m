function[BFS , A]=simp_min(A, BV , cost , variables)
zjcj = cost(BV)*A-cost;
run=true;
while run
    zcj = zjcj(1:end-1);
    if any(zcj>0)
        fprintf('Current soln is not optimal\n');
        [ent_col , pvt_col]=max(zcj);
        fprintf('Entering column: %d \n',pvt_col);
        Sol=A(:,end);
        column= A(:,pvt_col);
        if column<=0
            error('The LPP is unbounded')
        else
            for i=1:size(A,1)
                if column(i)>0
                    ratio(i)=Sol(i)./column(i);
                else
                    ratio(i)=inf;
                end
            end
            [MinRatio, pvt_row]= min(ratio);
            fprintf('The leaving row is %d\n', pvt_row);
        
            BV(pvt_row)=pvt_col;
            pvt_key = A(pvt_row, pvt_col);
            A(pvt_row,:)=A(pvt_row,:)./pvt_key;
            for i=1:size(A,1)
                if i~= pvt_row
                   A(i,:)=A(i,:)-A(i,pvt_col).*A(pvt_row, :);
                end
            end
            zjcj = cost(BV)*A-cost;
            zcj=[zjcj ; A];                          % Simplex Table
            table= array2table(zcj);
            table.Properties.VariableNames(1:size(zcj,2))=variables
            BFS(BV) = A(:,end);
        end
    else
        run=false;
        fprintf('The current BFS is optimal\n');
        fprintf('End of Phase \n')
        BFS=BV;
    end
end
end



