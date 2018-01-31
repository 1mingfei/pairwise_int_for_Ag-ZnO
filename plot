#!/usr/bin/gnuplot
set terminal postsc eps enhanced color font ",30"
set output "b.eps"
set xlabel "r(A)"
set ylabel "phi(r)(eV)"
set xrange [0.8:6]
set yrange [-0.75:1.0]

plot 'L-J-Ag-O.0.2' using 1:2 w l title "Ag-sub 0.2eV",\
     'L-J-Ag-O.0.4' using 1:2 w l title "Ag-sub 0.4eV",\
     'Ag-Ag.int' using 1:2 w l title "Ag-Ag",\
     'L-J-X.tmp' using 1:2 w l title "substrate",\

#plot 'Ag-Ag.int' using 1:($2)/($1) w l title "Ag-Ag(ref)",\
