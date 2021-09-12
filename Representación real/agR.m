FieldDR=[inferiorX inferiorY; superiorX superiorY];
%Genera poblacion inicial
cromosomas=crtrp(tamanoPoblacion, FieldDR);
[aptitudesRelativas, cromosomaElitista, aptitudElitista, aptitudPoblacion]=evaluar1(tamanoPoblacion, cromosomas, opcionFuncion, opcionSeleccion);
for j=2:generaciones+1
	cromosomas=seleccionar(tamanoPoblacion, cromosomas, aptitudesRelativas, opcionSeleccion);
	%Cruza
	cromosomas=reclin(cromosomas);
	%cromosomas=recint(cromosomas);
	%Muta
	cromosomas=mutbga(cromosomas, FieldDR, [1/2 1.0]);
	[aptitudesRelativas, cromosomaElitista, aptitudElitista, aptitudPoblacion]=evaluar2(tamanoPoblacion, cromosomas, opcionFuncion, cromosomaElitista, aptitudElitista, opcionSeleccion);