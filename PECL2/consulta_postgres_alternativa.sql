-- Debido a que el tipo money interactúa de forma extraña a la hora hacer comparaciones con él, la siguiente consulta
-- al ejecutarla en uno de nuestro ordenadores no devolvía nada, pero en el otro funcionaba correctamente.
-- Se adjunta este archivo adicional porque hace la consulta sobre el tipo money directamente sin castearlo a numeric.

select distinct "Musicos"."Nombre", "Musicos"."Codigo_grupo_Grupo"
from "Musicos" inner join "Grupo" on "Musicos"."Codigo_grupo_Grupo"="Grupo"."Codigo_grupo"
inner join "Grupos_Tocan_Conciertos" on "Grupo"."Codigo_grupo"="Grupos_Tocan_Conciertos"."Codigo_grupo_Grupo"
inner join "Conciertos" on "Grupos_Tocan_Conciertos"."Codigo_concierto_Conciertos"="Conciertos"."Codigo_concierto"
inner join "Entradas" on "Conciertos"."Codigo_concierto"="Entradas"."Codigo_concierto_Conciertos"
inner join "Discos" on "Grupo"."Codigo_grupo"="Discos"."Codigo_grupo_Grupo"
inner join "Canciones" on "Discos"."Codigo_disco"="Canciones"."Codigo_cancion"
where "Conciertos"."Pais"='Spain' and "Entradas"."Precio" <= '50.00' and "Entradas"."Precio" >= '20.00'
and "Discos"."Genero"='rock' and "Canciones"."Duracion" > '03:00:00' 
and "Musicos"."Codigo_grupo_Grupo" in (select "Codigo_grupo_Grupo"
                                            from "Musicos"
                                            group by "Codigo_grupo_Grupo"
                                            having (count("codigo_musico")>3));