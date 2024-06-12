# Laboratorio N° 4 -  Diseño de tests funcionales de APIS

Laboratorio para la cátedra "Tecnología e Ingeniería Web", correspondiente a la carrera Ingeniería Informática de la Universidad Nacional de Catamarca.

# Consignas

Implementar los siguientes tests en el proyecto Django de desarrollo de APIS:

1. Verificar que al ejecutar el endpoint de recuperación de una orden, se devuelven los
datos correctos de la orden y su detalle.

2. Verificar que al ejecutar el endpoint de creación de un detalle de orden, ésta se cree
correctamente, controlando que se haya actualizado el stock de producto relacionado.

3. Verificar que al ejecutar el endpoint de creación de un detalle de orden, cuando se
agrega un producto que ya está en otro detalle de la misma orden, se sume la cantidad
de productos total para la orden y no existan dos registros de detalle orden con el
mismo producto.

4. Verificar que al ejecutar el endpoint de creación de un detalle orden, se produzca un
fallo al intentar procesar la cantidad de un producto que sea mayor al stock de ese
producto.

5. Verificar que al ejecutar el endpoint de eliminación de una orden, ésta se haya
eliminado de la base de datos correctamente, junto con sus detalles, y que, además
se haga incrementado el stock de producto relacionado con cada detalle de orden.

6. Verificar que el método get_total de una orden, devuelve el valor correcto de acuerdo
al sub-total de cada detalle.

7. Verificar que el método get_total_usd de una orden, devuelve el valor correcto de
acuerdo al total de la orden y la cotización del dólar blue (considerar “mockear” el valor
del dólar blue, simulando la respuesta de la API externa).