
function M = zigzag(n)
    M = zeros(n,n);
    states = 1:4; #
    x = 1;
    y = n;
    state = 1;
    for i = 1:(n*n)
        if x!=0 && y!=0
          M(y, x) = i
        elseif x==0 && y!=0
          x++
          M(y, x) = i
        elseif x !=0 && y ==0
          y++
          M(y, x) = i
        elseif y>n
            y--
            M(y, x) = i
        elseif x>n
            x--
            M(y, x) = i
        endif
        if state == 1
            x++
            if y==1
                state = states(4)
            else
                state = states(3)
            endif
        elseif state == 2
            --y
            if x==1
                state = states(4)
            else
                state = states(3)
            end
        elseif state == 3
            x--
            y--
            if x==1
                state = states(2)
            elseif y==1
                state = states(1)
            end
        elseif state == 4
            x++
            y++
            if y == n
                state = states(1)
            elseif x == n
                state = states(2)
            end
        end
    endfor
    rot90(M, 2)
end

