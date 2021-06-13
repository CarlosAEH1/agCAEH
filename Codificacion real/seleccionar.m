function [cromosomasSeleccionados]=seleccionar(tamanoPoblacion, cromosomas, aptitudesRelativas, opcionSeleccion)
	aptitudAcumulada=0;
    %Calcula aptitud acumulada
	for i=1:tamanoPoblacion
		aptitudAcumulada=aptitudAcumulada+aptitudesRelativas(i);
		aptitudesAcumuladas(i)=aptitudAcumulada;
    end
    %Selecciona cromosomas
    for i=1:tamanoPoblacion
        aleatorio=rand;
		for j=1:tamanoPoblacion
			if aptitudesAcumuladas(j)>aleatorio
 				switch opcionSeleccion
                    case 1
                        %Maximizacion de aptitud acumulada
                        cromosomasSeleccionados(i, :)=cromosomas(j, :);
                    case 2
                        %Minimizacion de aptitud acumulada
                        if j==1
                            cromosomasSeleccionados(i, :)=cromosomas(j, :);
                        else
                            cromosomasSeleccionados(i, :)=cromosomas(j-1, :);
                        end
                end
                break
            end
        end
	end