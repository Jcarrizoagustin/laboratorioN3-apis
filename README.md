# Laboratorio N° 3 -  Desarrollo de Apis con Django

Laboratorio para la cátedra "Tecnología e Ingeniería Web", correspondiente a la carrera Ingeniería Informática de la Universidad Nacional de Catamarca.

# Consignas

Crear una API REST utilizando DJANGO REST FRAMEWORK, que brinde la siguiente
funcionalidad básica y acotada de un E-commerce.
1. El sistema debe tener los modelos Producto, Orden, DetalleOrden con los siguientes
atributos:
    **Producto:**
    - id PK
    - nombre [string]
    - precio [float]
    - stock [int]

    **Orden:**
    - id PK
    - fecha_hora [datetime]
    
    **DetalleOrden:**
    - orden [Orden]
    - cantidad [int]
    - producto [Producto]

2. El API REST debe proporcionar los siguientes end-points:
a. Registrar / Editar / Eliminar un producto
b. Consultar un producto / Listar todos los productos
c. Registrar / Editar datos de una orden.
d. Eliminar una orden. Tener en cuenta que se debe restaurar stock de los productos
asociados a esa Orden.
e. Registrar / Editar Detalle de Orden. Se debe actualizar el stock del producto en
base al nuevo valor ingresado en “cantidad”
f. Consultar una orden y sus detalles
g. Listar todas las órdenes

3. La clase Orden debe exponer un método get_total el cual calcula el total de la
operación y debe retornar ese valor en el serializador correspondiente. También debe
exponer el método get_total_usd, utilizando el API de
https://dolarapi.com/v1/dolares/blue, para que devuelva el precio en dólares.

4. Al crear o editar un detalle de orden, se debe validar:
* que la cantidad de cada producto sea mayor a 0
* que haya suficiente stock del producto de acuerdo a la cantidad ingresada
* que no se repitan productos en la misma orden. En ese caso, adicionar las
cantidades para un mismo producto
5. Para la implementación del API se pueden utilizar cualquiera de las Vistas repasadas
en clase: ApiView, Generic View, ModelViewSet, etc.

6. El código fuente del API debe ser subido a un repositorio público, el cual debe ser
proporcionado para su correcta examinación.