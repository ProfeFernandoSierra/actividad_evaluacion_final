Un Centro Médico desea implementar un sistema informático para la atención de sus pacientes, y para ello, le solicitan a usted que desarrolle lo especificado a continuación ↓
Se le solicita crear un menú en el cual se pueda registrar la ficha médica de un paciente, los atributos que debe tener la ficha son los siguientes:
⮚	Rut, sin dígito verificador ni puntos.
⮚	Nombre
⮚	Dirección
⮚	Correo 
⮚	Edad (número entero entre 0 y 110)
⮚	Sexo, solo puede aceptar como caracteres las letras f o m
⮚	Registros
⮚	Prevision Salud, acepta sólo que se ingrese Isapre o Fonasa (no es necesario especificar la Isapre)

El menú debe tener las siguientes opciones ↓
 
				Centro Médico DUOC
1) Registrar Paciente
2) Atención Paciente
3) Consultar Datos Paciente
4) Salir

Donde Registrar Paciente solicite todos los datos de un paciente para hacer registro de una nueva ficha, cada uno de los atributos debe cumplir con lo solicitado (validación mediante ciclos),
●	Rut debe ser un número entero que se encuentre dentro del rango de 5000000 y 99999999.
●	Edad debe ser un número entero que se encuentre en el rango 0 y 110.
●	Sexo debe ser un carácter que sólo acepta la letra f o m (mayúscula y minúscula).
●	PS debe ser una cadena de caracteres que sólo acepta los valores “ISAPRE” y “FONASA”
●	Correo Debe ser una cadena de caracteres que contenga al menos un carácter “@”, ejemplo → juan@lopez.

Atención Paciente Deberá en primera instancia solicitar el Rut del paciente, luego verifica que el Paciente se encuentre registrado en el sistema, una vez validado se le solicitará ingresar la fecha y las observaciones de la visita, y lo concatenará con los registros anteriores con el nuevo registro.

Consultar Datos Paciente Muestra por pantalla todos los atributos del paciente que coincida con el Rut ingresado, los datos se deben mostrar de forma ordenada, para ello utiliza herramientas de tabulación y saltos de línea según lo aprendido en clases, también de forma adicional puede usar caracteres especiales.

Salir, debe salir del ciclo del menú y mostrar un mensaje “Ha salido del sistema…”
