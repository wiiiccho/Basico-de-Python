Comando JOIN
-- Cuenta cuanos datos tenemos en existencia
SELECT COUT(*) FROM cliente;

SELECT *FROM cliente WHERE id > 0 AND id <= 5;
SELECT *FROM cliente WHERE id BETWEEN 1 AND 5;
SELECT nombre, apellido FROM cliente WHERE id BETWEEN 1 AND 5;

Comando JOIN
Primer paso para formarlo
SELECT FROM categoria AS c JOIN producto AS p ON c.id = b.id_categoria;
Segundo paso para formarlo pedir los datos que quiero que me lo muestre en este caso pido tres columnas
SELECT c.id, c.nombre, p.nombre FROM categoria AS c JOIN producto AS p ON c.id = b.id_categoria;
Luego ponemos la condicion de cuantos datos quiremos que me lo muestre
SELECT c.id, c.nombre, p.nombre FROM categoria AS c JOIN producto AS p ON c.id = b.id_categoria where b.id_categoria BETWEEN 1 AND 5;


SELECT c.nombre, l.titulo, t.tipo FROM transaccion 
AS t JOIN libros  AS l ON t.id = b.id_libros JOIN cleinte AS C
 ON t.id = c.id_cliente


SELECT c.nombre, l.titulo, t.tipo FROM transaccion 
AS t JOIN libros  AS l ON t.id = b.id_libros JOIN cleinte AS C
 ON t.id = c.id_cliente where c.gender = 'f' AND AND t.tipo = 'sell';

SELECT c.nombre, l.titulo, t.tipo FROM transaccion 
AS t JOIN libros  AS l ON t.id = b.id_libros JOIN cleinte AS C
 ON t.id = c.id_cliente 
 where c.gender = 'f' AND  t.tipo IN ('SELL', 'LEND');

Left JOIN
SELECT b.titulo, a.nombre FROM libros AS l INNER JOIN autores AS a ON a.id = b.ciente_id LIMIT 10;

SELECT c.id, c.nombre, p.nombre FROM categoria 
AS c JOIN producto AS p ON c.id = b.id_categoria
 where b.id_categoria BETWEEN 1 AND 5 ORDER BY b.id_categoria;

 SELECT c.id, c.nombre, p.nombre FROM categoria 
AS c JOIN producto AS p ON c.id = b.id_categoria
 where b.id_categoria BETWEEN 1 AND 5 ORDER BY b.id_categoria DESC;

  SELECT c.id, c.nombre, p.nombre FROM categoria 
AS c LEFT JOIN producto AS p ON c.id = b.id_categoria
 where b.id_categoria BETWEEN 1 AND 5 ORDER BY b.id_categoria DESC;

  SELECT c.id, c.nombre, p.nombre FROM categoria 
AS c LEFT JOIN producto AS p ON c.id = b.id_categoria
 where b.id_categoria BETWEEN 1 AND 5 ORDER BY b.id_categoria DESC;	
