# las formas de despliegue son vps o Paas="Platform as a services"

# Integracion y despliegue continuo => CI/CD => Continues integration - continues deployment

# 1 - comprar dominio = namecheap.com
# 1.1 - apuntar dominio a ip = domainlist - advanced DNS
# 1.2 - ver si mi dominio se esta propagando = www.whatsmydns.net


# 2 - vps = hostinger = codigo descuento = HOLAMUNDO
# 2.1 - OPCION APLICATION - I want to choose a different Control panel


# 3. - certificado SSL  - los numeros son la ip de mi servidos
# en consola ssh root@45.90.223.77 - yes - password => con esto entramos al servidor
# ponemos dominio son www
# para agregar el certificado damos email- password y decimos si al https


# 4. - github y requirement - 
# en consola pip freeze > requirements.txt    => esto creara un archivo con todas las dependencias


# 5. - llaves SSH para github-
# en consola ssh-keygen -t rsa -b 4096 -C "micorreo@gmail.com"     -- esto entregara una llave publica y privada en una ruta
# se da enter a todo lo que pide sin dar datos
# vamos a la ruta para obtener las llaves y la que tiene .pub lo abrimos, seleccionamos todo 
# y en github en settings - SSH and GPG keys - new SSH keys
# titulo para el dispositivo donde lo hago - y la key

# en el servidor para indicarle que puede confiar en esa llave le indicamos la ruta y el comando de autorizar un ejemplo seria el siguiente
# cat .ssh/id_rsa.pub > .ssh/authorized_keys

# para ver el contenido de la llave publica se ejecuta
# cat .ssh/id_rsa.pub o cat ~/.ssh/id_rsa.pub
# en este caso para que el traiga directametne no vamos a config sino al repositorio a desplegar - settings - deploys keys - add deploy keys
# le damos titulo y key

# desde consola GESTIONAR VERSIONES de python si tengo 3.10.6 y quiero 3.11
# apt update                                                                        => actualiza repositorios del servidor
# apt list | grep python3.11                                                        => ver versiones disponibles
# apt install python3.11                                                            => instalar python
# update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2      => indicar arternativa versiones
# update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1      => indicar arternativa versiones
# update-alternatives --config python3          => nos entrega una pregunta y seleccionamos opcion


# esto no se si aplique a otros servidores. este es el caso de hostinger
# ufw allow 7080                     => habilitar puerto que es el que usa el servidor web
# cat /root/.litespeed_password      => obtener contraseña panel de administrador
# urldominio:7080                    => autorizamos la advertencia de seguridad, entramos a un panel de administrador y usuario es admin, contraseña la que obtuvimos
# opcion virtual hosts - example - context - app server - editar - aqui hay un formulario el cualcambiaremos todos los demo por carpeta_proyecto
# location - "demo" se cambia por "carpeta_proyecto"
# startup File - "demo" se cambia por "carpeta_proyecto"
# Environment - "demo" se cambia por "carpeta_proyecto"
## ahora vamos a la carpeta activamos el entorno virtual e instalamos dependencias
# cd /usr/local/lsws/Example/html/carpeta_proyecto
# source /usr/local/lsws/Example/html/bin/activate
# pip install -r requirements.txt



# AUTOMATIZAR DESPLIEGUE CON GITHUB ACTIONS
