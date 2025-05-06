workers = 4 # Número de trabajadores
bind = "0.0.0.0:8000" #Escucha en todas las interfaces de red
chdir = "/home/juarez/desktop/repositorio/laboratorioN3-apis" # Cambia al directorio del proyecto
module = "ecommerce.wsgi:application" # Nombre del módulo WSGI
timeout = 120 # Tiempo de espera para las solicitudes

# Configuración de los registros
accesslog = "-" # Registros de acceso en la salida estándar
errorlog = "-" # Registros de error en la salida estándar

