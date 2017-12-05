#!/usr/bin/gnuplot
set terminal postsc eps enhanced color
set output "a.eps"
set xlabel "r(A)"
set ylabel "r*phi(r)(ev-A)"
set xrange [0.8:6]
set yrange [-2.5:2.0]

plot 'Ag-Ag.int' using 1:2 w l title "Ag-Ag(ref)",\
     'L-J-Ag-O.tmp' using 1:3 w l title "Ag-sub",\
     'L-J-X.tmp' using 1:3 w l title "substrate",\

