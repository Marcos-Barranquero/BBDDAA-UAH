-- Archivo de consultas que prueban que la seguridad funciona correctamente, está pensado para ir haciendo 
-- las consultas de 1 en 1 y no ejecutando el archivo entero.

-- PRUEBAS ACCESO A TABLAS --
SET ROLE productor1;
SELECT * FROM "Entradas";       -- Debería funcionar
UPDATE "Entradas" SET "Usuario"='Pepe' WHERE "Codigo_entrada"=1;    -- Debería dar error
INSERT INTO "Grupo" VALUES(1,'grupo1','rock','spain','www.grupo1.es');  -- Debería funcionar


SET ROLE musico1;
SELECT * FROM "Entradas";   -- Debería dar error
INSERT INTO "Grupo" VALUES(2,'grupo1','rock','spain','www.grupo1.es');  -- Debería dar error


SET ROLE organizador1;
SELECT * FROM "Entradas";   -- Debería funcionar
UPDATE "Entradas" SET "Usuario"='Pepe' WHERE "Codigo_entrada"=1;    -- Deberia funcionar


SET ROLE admin;
SELECT * FROM "Entradas";      -- Debería funcionar
UPDATE "Entradas" SET "Usuario"='Antonio' WHERE "Codigo_entrada"=1;     -- Debería funcionar
INSERT INTO "Musicos" VALUES(400,'12353464L','nombre1','direccion1',29983,'Madrid','Comunidad de Madrid',676789012,'triangulo',1); -- Debería funcionar

-- PRUEBAS RLS --

-- Desde una cuenta de tipo Musico
SET ROLE nombre1;
SELECT * FROM "Musicos";    -- Deberia devolver solo el valor cuyo nombre=nombre1
UPDATE "Musicos" SET "Ciudad"='Albacete';   -- Deberia actualizar solo el valor de la ciudad para el musico con nombre=nombre1
SELECT * FROM "Musicos";    -- Para comprobar que el update ha funcionado correctamente

-- Desde una cuenta de tipo Administrador
SET ROLE admin;
UPDATE "Musicos" SET "Ciudad"='Coslada';   -- Deberia actualizar las ciudades de todos los músicos
SELECT * FROM "Musicos";    -- Deberia devolver toda la tabla
