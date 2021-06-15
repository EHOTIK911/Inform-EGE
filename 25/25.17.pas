var
    numDel, i, j: longint;
    d2: array[1..6] of longint;
begin
    for i := 95632 to 95650 do begin
        numDel := 0;
        for j := 1 to i do begin
            if (i mod j = 0) and (j mod 2 <> 0) then begin
                numDel := numDel + 1;
                if numDel > 6 then break;
                d2[numDel] := j;
            end;
        end;
        if (numDel = 6) then writeln(d2[1], ' ', d2[2], ' ', d2[3], ' ', d2[4], ' ', d2[5], ' ', d2[6]);
    end;
end.
