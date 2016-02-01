# LibertySpeedTestReportScript
Script en Python que realiza un SpeedTest y notifica a Liberty Puerto Rico cuando las velocidades no son las indicadas. El script esta hecho para Liberty Puerto Rico pero usted puede adaptarlo a su proveedor de servicio de internet deseado.

Requisitos:

-El script está hecho para Raspbian del Raspberry Pi, pero deberia funcionar con cualquier distro de linux, pero tendras que editar ciertas partes del codigo en donde se hace referencia a /home/pi/Documents, cambiando /pi/ por el nombre de usario en Linux
-Python (Lo probé con el Python que trae Raspbian preinstalado)
-Speedtest-cli, lo consigues en https://github.com/sivel/speedtest-cli
-Si no tienes "requests" de python lo puedes instalar escribiendo en el terminal "pip install requests"
-Un app en Facebook para postear en la pagina de Liberty
Localizaciones por defecto:

-Speedtest-cli está localizado en el script en /home/pi/Documents/speedtest-cli.py
-El archivo CSV que almacena la data de las pruebas está localizado en /home/pi/Documents/ y lleva por nombre data.csv
Pasos a seguir:

1. Deberas crear un app en facebook accediendo a http://developers.facebook.com
2. En el menu de "My Apps", oprima en "Add a new app"
3. Selecciona WWW en las opciones a seleccionar
4. Si ya tienes apps hechas en facebooks, oprime "Skip and Create App ID"
5. En Display Name entra un nombre que quieras usar para el app, puede ser cualquiera, pero el nombre que escojas sera visible en la pagina de Liberty, asi que ten consideracion de lo que escribas ahi.
6. En la categoria, selecciona cualquiera. Yo seleccione "Apps for Pages".
7. En la pagina que veras ahora, podras ver el App ID y el App Secret. Estos datos los utilizaremos luego.
8. Ve a Settings y escribe un email de contacto. Debes entrar un email o de lo contrario no podras seguir con el proximo paso
9. Ve a App Review y en donde dice "Do you want to make this app and all its live features available to the general public?" marca que sí
10. Confirma el mensaje que te aparece que dice "Are you sure you want to make your app public? It will become available to everyone."
11. Ahora, accede a https://developers.facebook.com/tools/explorer
12. En "Application" selecciona el app que recien creaste
13. En "Get Token" selecciona "Get User Access Token"
14. en los permisos, selecciona "user_status" en la pantalla que se muestra. Luego, selecciona el tab de "Extended Permissions" y marca "manage_pages" y "publish_actions"
15. Confirma
16. Veras unas ventanas pidiendo permiso para utilizar tu cuenta. Uno de ellos dice "NOMBRE DEL APP will receive the following info: your public profile and status updates". Oprime Okay
17. La proxima ventana para confirmar dice: "test would like to post to Facebook for you. Who do you want to share these posts with?". Selecciona "Public" ya que estaremos posteando a una pagina de facebook. Luego oprime Okay
18. "test would like to manage your Pages.", oprime Okay. Esto es por si acaso ya que el app que creaste no accede a tus paginas pero sí estará posteando a una.
19. Veras que se generó el Access Token. Copia esto precionando CTRL+C en el teclado
20. Ahora es que utilizaremos el App ID, Secret ID y el Access Token. Necesitas entrar l siguiente direccion y sustituir {APP_ID} por el App ID de la aplicacion que creaste, {APP_SECRET} por el Secret ID del app que create, y {ACCESS_TOKEN}por el Access Token que el Graph API Explorer te generó en el siguiente URL, eliminando los brackets {} solo dejando la combinacion de numeros y letras para cada cosa
https://graph.facebook.com/oauth/access_token?client_id={APP_ID}&client_secret={APP_SECRET}&grant_type=fb_exchange_token&fb_exchange_token={ACCESS_TOKEN}
21. Preciona enter en el teclado para entrar a la direccion que recien cambiaste los datos necesarios
22. Veras que sale "access_token=....." deberas copiar SOLAMENTE el string que se muestra luego de "access_token="
22. Ahora, abre el Script de Python, busca donde dice "face=token = 'YOUR_ID' y cambia YOUR_ID por el access_token que Facebook generó, pero tienes que dejar las comillas que tiene 'YOUR ID' en el principio y al final, de lo contrario no va a funcionar.
23. Tambien deberás cambiar el mensaje y el criterio de evaluación en los "elif eval(d)". Actualmente el valor que está es de 30, pero lo puedes cambiar a la velocidad que quiera.
24. Los mensajes a cambiar son los que estan luego de "post" Actualmente los mensajes por defecto son los siguientes:

post = 'Hola Liberty, por que no tengo internet? Pago por 40down\\4up en Carolina... Por favor resuelvanme!!'
post = 'Hola Liberty, por que mi velocidad de internet es " + str(int(eval(d))) + "down\\" + str(int(eval(u))) + "up cuando pago por 40down\\4up en Carolina... Por favor resuelvanme!!'
post = 'Hola Liberty, Gracias por ofrecerme un servicio de excelencia. Pago por 40down\\4up en Carolina y estoy recibiendo la velocidad completa.'

asi que lo que tienes que cambiar es la seccion donde dice "40down\\4up en Carolina" por la velocidad que tienes ahora mismo y el pueblo en donde te encuentras. Es necesario que entre la velocidad de Download y Upload hayan doble slash \\ de lo contrario no va a funcionar

23. Graba el Script de Python con el cambio realizado
24. Ahora abre un terminal en Raspbian y escribe "python NOMBRE_DEL_SCRIPT" para correrlo.
25. Si todo sale bien el script escribira un post en la pagina de liberty.


El credito va para el creador de este tremendo codigo: http://pastebin.com/WMEh802V
Noticia donde se hace referencia al codigo: http://thenextweb.com/shareables/2016/01/31/frustrated-comcast-customer-sets-up-bot-to-tweet-complaints-every-time-internet-speed-drops/
