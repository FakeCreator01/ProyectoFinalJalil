NOTASWEB es una app creada por Franco Jalil donde los usuarios podrán crear, editar, borrar y visualizar sus notas. 

Los usuarios sólo podrán ver sus notas, no tienen acceso a ver notas de otros usuarios de la plataforma. 

  

## VIDEO EXPLICATIVO DE LA WEB ## 

https://www.youtube.com/watch?v=HPJeDEjTu00
  

## Se utilizaron las siguientes tecnologías ## 

  

-Python 3.10.3 

-Django 4.0.5 

-CSS 

-HTML 

  

## Detalles técnicos de la app (Configuración en Django) ## 

El proyecto se nombró cómo 'src' por convención. 

  

  

** APPS ** 

Se utilizaron tres apps: 'inicio', 'usuario' y 'nota'. 

  

** MODELOS ** 

- App usuario: 

Se utilizó el modelo por defecto que trae django 'User' 

  

- App nota: 

Se creó un modelo 'Nota' con un título, subtitulo, texto, imagen, fecha y usuario. 

  

** FORMULARIOS ** 

- App usuario: 

Se utilizó el formulario por defecto de Django 'UserCreationForm' 

  

- App Nota: 

Se utilizó la herencia 'ModelForm' para crear un formulario automáticamente con el modelo 'Nota'. Los campos visibles son: 'titulo', 'subtitulo', 'texto' y 'imagen'. Los campos 'fecha' y 'usuario' se completarán automáticamente cuando el usuario cree dicho formulario. 

  

** VISTAS ** 

-- Se utilizaron vistas basadas en clases. 

  

- App Inicio: 

Se crearon las vistas 'Inicio' y 'AcercaDe' 

  

- App usuario: 

Se crearon las vistas 'Login', 'Signup' y 'Logout'. Donde la vista 'Logout' se crea por defecto importándola en views.py. 

  

- App Nota: 

Se crearon las vistas necesarias para un CRUD: 'ListaNotas', 'CrearNota', 'VerNota', 'EditarNota' y 'EliminarNota'. 

Todas estas vistas tienen el mixin 'LoginRequiredMixin' así sólo los usuarios logeados pueden acceder. 

Además, se agregó la lógica para que los usuarios sólo puedan ver sus notas (las de nadie más) en la view 'ListaNotas' 

  

** URLS Y LINKS ** 

  

En las urls del proyecto 'src' están incluidas las urls de las tres apps. 

  

- App Inicio: 

Se crearon dos urls: una para el inicio y otra para la página 'acerca de'.  

Para acceder al inicio '/' 

Para acceder a 'Acerca De' '/acerca-de/' 

  

  

- App usuario: 

Se crearon las 3 urls necesarias para la autenticación: 

La de registro '/signup/' 

La de login '/login/' 

La de logout '/logout/' 

  

- App Nota: 

Se crearon las cinco urls necesarias para el CRUD: 

Lista de mis notas '/mis-notas/' 

Crear nota '/crear-nota/' 

Ver nota '/ver-nota/' 

Editar nota '/editar-nota/id_nota' id_nota = id del objeto 'Nota' 

Eliminar nota '/eliminar-nota/id_nota' 

  

** TEMPLATES ** 

Se creó una carpeta 'templates' dentro del proyecto donde está el archivo padre 'base.html' donde se cargan los archivos estáticos y se hace la estructura base del proyecto. 

También están los templates de 'inicio' donde se mostrará un mensaje de bienvenida y algunos atajos para la web,  y el template 'acerca-de' donde se muestra una breve introducción a mi persona y al proyecto. 

  

Se crearon 3 sub-carpetas: 

- snippets: donde se almacenan los bloques de codigo importantes. En este caso se encuentra el archivo 'navbar.html' (que se incluye en el archivo padre) 

  

- nota: donde se almacenan los cinco templates necesarios para el crud: crear-nota.html , editar-nota.html , eliminar-nota.html , lista-notas.html y ver-nota.html 

  

- usuario: donde se almacenan dos templates: 'login.html' y 'signup.html' 

  

** ARCHIVOS MEDIA Y ESTATICOS ** 

Se crearon dos carpetas dentro del proyecto: 

- 'static': donde se almacena la carpeta 'css' y dentro de ésta el archivo 'styles.css' 

  

- 'media': donde se almacenan los archivos tipo media. Dentro de esta carpeta hay dos sub-carpetas. Una para guardar el favicon y otra para guardar las imágenes de las notas de los usuarios (llamada 'imagen_nota') 

 