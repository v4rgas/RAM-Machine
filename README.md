# RAM-Machine
Este proyecto busca simular una máquina RAM con una interfaz gráfica para mejorar la experiencia del usuario :D.
>
[¿Que es?](https://en.wikipedia.org/wiki/Random-access_machine)
>
Se pueden usar los comandos ```dec(r)```, ```inc(r)```, ```goto(r)```, ```halt()```, ```clear(r)```, ```move(r, s)```, ```copy(r, s)``` y ```add(r, s, t)```. 
>
Para correr la interfaz es necesario correr ```GUI.py```, dado que este corre por sí solo ```ram.py```.
>
**Programa de ejemplo :eggplant:**
>
![alt text](https://github.com/v4rgas/RAM-Machine/blob/main/example/example1.png?raw=true)
>
No nos hacemos responsables por posibles errores :confused:

**Ahora tenemos versiones ejecutables para Windows y Linux**


* Funciones:

    * DEC(r): si r>0, entonces r-=1 y PC+=2; SINO PC += 1
    * INC(r): Aumento en 1 el registro r
    * GOTO(R): PC = r
    * HALT(): Dentiene programa, output en el registro 0
    * CLEAR(r): Hace que el registro r se quede en 0, * luego sigue con la siguiente instruccion
    * MOVE(r, s): Mueve el valor del registro r al registro s, deja el registro r igual a 0

    * COPY(r, s): Copia el valor del registro r al registro s

    * ADD(r, s, t): Suma el registro r al registro s y t, luego hace el registro r = 0 
>
* Consideraciones:
    * PC corresponde a la linea de codigo que el programa esta ejecutando, y este comienza en la primera linea (PC = 0)
    * Despues de cada funcion ejecutada, suce que PC += 1
    * El cuadro de texto inferior corresponde a el registro inicial
