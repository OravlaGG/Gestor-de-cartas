<div align="center"> 
  
# $\color{Gold}{PROYECTO\ -\ DJANGO\ Alvaro\ Gomez}$
</div>

En este repositorio encontraremos mi primera aplicación creada con Django usando Bootstrap para hacer un pequeño estilo, la idea original es hacer un pequeño gestor de cartas para el famoso juego de cartas Magic the Gathering.

Para poner en funcionamento la app hace falta python y Django instalados en el sistema. Luego descarga el repositorio y ya apartir de alli nos pondremos con la funcionalidad.
Tambien se creo la migración para el personaje para que asi exista la tabla que hace falta para que toda la aplicación funcione. Ya una vez con eso podras crear tus super usuarios y usuarios que quieras pero primero explicare un poco tambien como funciona.
Para aquel que no le interese o le de igual lo que escriba aqui os pondre las credenciales de tanto un SuperUsuario como el de un usuario normal.

<h3>Super</h3>
Nombre: "admin"

Pass: "1234"

<h3>Usuario</h3>
Nombre: "prueba"

Pass: "Prueba.Prueba"

<div align="center"> 
  
# $\color{Purple}{Modelos}$
</div>

Bueno si estas aqui es porque te interesa un poco lo que tengo que explicar o eres mi profesora que me va a evaluar el proyecto, en cualquieras de los casos comencemos.

Primero que todo el proytecto consiste de 4 modelos diferentes todos ellos conectados entre si, aparte de esto aprovecho el modelo de usuario que ofrece Django para unirlo a otro de los modelos más inferiores en la escala.

Los dos modelos bases que tiene conexion con los inferiores y son el modelo de las "Ediciones" y el de los "Colores". Para explicarlo y que se entienda magic tiene lo que se conocen como colores de cartas que simbolizan una forma de juego y el tipo de mana que consume y las 
ediciones son colecciones de cartas que van saliendo cada X meses tyrayendo cartas nuevas o algunas creadas anteriormente. Aparte de essto último, las cartas 
tambien pueden ser de multiples coleres y de diferentes tipos aunque esta última no la inclui porque no complicar demasiado los modelos. 

Por debajo de estos 2 modelos encontramos el modelo de "Cartas" que esta unido por una relación de ManytoMany a ambos modelos que explique antes. Junto a ello hay demas datos que son más de relleno y para hacer un poco más boluminosas las tablas pero que existen dentro de las cartas.

El último modelo "Coleccion" esta unido a otros 2, el de las "Cartas" y el de "User", este es el que viene por defecto en Django, para tu poder añadir una carta a tu coleccion necesitas tener un usuario por obvias razones. En este ultimo modelo aparece la información
principal de la carta su condición de si esta nueva, gastada, dañada... y la cantidad de cartas que puedes tener de ese tipo siendo su minimo 1. Para crear
cada una de las cartas en la colección se usa las PK de las cartas existentes con la PK del Usuario usandolo como FK ambas.

<div align="center"> 
  
# $\color{Purple}{Funcionamiento}$
</div>

Con los modelos ya explicados pasare al apartado de funcionamiento y de reactividad que he añadido a la web. 

La primera vez que entras en la pagina solo te apareceran 2 links que son el de Cartas y el de Login, esto esta pensado para que no se intenten meter en colleciones que no existen porque no estan logueados.
Una vez que te logues el login desaparecera y aparecera el Logout y la colección del usuario logueado, junto a esto en la pagina de las cartas te aparecera para poder añadir cartas a tu colección, solo es cuando estas logueado
ya que si no lo añadiria a alguien que no existe. Junto a todo esto tambien durante el login si por algun motivo te equivocas el sistema te lo hara saber con mensajes de igual manera que cuando tye hayas deslogueado de manera existosa.

<h3>Colección</h3>
En el apartado de coleccion no puedes crear cartas como tal porque solo existen las que existen, se que quizas sea limitante para el usuario promedio pero es como funciona el juego.
Para tu poder añadir cartas a tu colección debera de ser creadad anteriormente por el administrador del sistema. Una vez que esten en la tabla principal podras clicar a añadir y se añadira a tu colección. Auque pulses multiples veces
solo se te añadira una vez, el resto de ellas hara que aumente el nnúmero de la misma carta en propiedad.

Si nos metemos en la coleccion tendremos las cartas que hayamos añadido y 2 acciones, eliminar y editar. La primera es simple de entender eliminas de la lista de cartas la que selecciones. La de editar
te da la posibilidad de cambiar el estado de la carta y la cantidad total que tienes de la misma, ojo el minimo siempre sera 1 para eviatar errores.

<div align="center"> 
  
# $\color{Green}{Regla}$
</div>

Como reglas de negocio que elegi a petición del ejercicio ha sido la de evitar la repetición de la misma carta en la colección y la de evitar número en 0 o negativos. Como he explicado antes se evita 
en las vistas como en el imput que puede introducir el usuario en las páginas web
el añadir la misma carta 2 veces ya sea 
