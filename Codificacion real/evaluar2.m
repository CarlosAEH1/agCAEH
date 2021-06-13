function [aptitudesRelativas, cromosomaElitista, aptitudElitistaActual, aptitudPoblacion]=evaluar2(tamanoPoblacion, cromosomas, opcionFuncion, cromosomaElitista, aptitudElitistaAnterior, opcionSeleccion)
	funcion=0;
	for i=1:tamanoPoblacion
        %Evalua funcion
        switch opcionFuncion
            case 1
                funcion=-20*exp(-0.2*sqrt(0.5*((cromosomas(i, 1)^2)+(cromosomas(i, 2)^2))))-exp(0.5*(cos(2*pi*cromosomas(i, 1))+cos(2*pi*cromosomas(i, 2))))+exp(1)+20;
            case 2
                if i>=2
                    funcion=funcion+100*((cromosomas(i, 1)-cromosomas(i-1, 1)^2)^2)+(1-cromosomas(i-1, 1))^2;
                    aptitudesPoblacion(i-1)=funcion;
                    if i==tamanoPoblacion
                        funcion=funcion+100*((-cromosomas(i, 1)^2)^2)+(1-cromosomas(i, 1))^2;
                    end
                end
            case 3
                funcion=-(cromosomas(i, 2)+47)*sin(sqrt(abs((cromosomas(i, 1)/2)+cromosomas(i, 2)+47)))-cromosomas(i, 1)*sin(sqrt(abs(cromosomas(i, 1)-(cromosomas(i, 2)+47))));
            case 4
                funcion=((cromosomas(i, 1)^2+cromosomas(i, 2)-11)^2)+((cromosomas(i, 1)+cromosomas(i, 2)^2-7)^2);
        end
		aptitudesPoblacion(i)=funcion;
    end
    %Obtiene el mejor cromosoma
	switch opcionSeleccion
        case 1
            aptitudElitistaActual=max(aptitudesPoblacion);
            %Sustituye peor cromosoma por mejor cromosoma
            if aptitudElitistaAnterior>aptitudElitistaActual
                aptitudVulgar=min(aptitudesPoblacion);
                for i=1:tamanoPoblacion
                    if aptitudVulgar==aptitudesPoblacion(i)
                        cromosomas(i, :)=cromosomaElitista(1, :);
                        aptitudesPoblacion(i)=aptitudElitistaAnterior;
                    end
                end
                aptitudElitistaActual=aptitudElitistaAnterior;
            else
                for i=1:tamanoPoblacion
                    if aptitudElitistaActual==aptitudesPoblacion(i)
                        cromosomaElitista(1, :)=cromosomas(i, :);
                    end
                end
            end
        case 2
            aptitudElitistaActual=min(aptitudesPoblacion);
            %Sustituye peor cromosoma por mejor cromosoma
            if aptitudElitistaAnterior<aptitudElitistaActual
                aptitudVulgar=max(aptitudesPoblacion);
                for i=1:tamanoPoblacion
                    if aptitudVulgar==aptitudesPoblacion(i)
                        cromosomas(i, :)=cromosomaElitista(1, :);
                        aptitudesPoblacion(i)=aptitudElitistaAnterior;
                    end
                end
                aptitudElitistaActual=aptitudElitistaAnterior;
            else
                for i=1:tamanoPoblacion
                    if aptitudElitistaActual==aptitudesPoblacion(i)
                        cromosomaElitista(1, :)=cromosomas(i, :);
                    end
                end
            end
    end
    aptitudPoblacion=sum(aptitudesPoblacion);
    %Calcula aptitudes relativas
    for i=1:tamanoPoblacion
        aptitudesRelativas(i)=aptitudesPoblacion(i)/aptitudPoblacion;
    end