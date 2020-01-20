-- CREACION DE LOS ROLES DE USUARIO --
CREATE ROLE "Administrador" WITH
	CREATEROLE
	INHERIT
	REPLICATION;

CREATE ROLE "Productor";

CREATE ROLE "Organizador";

CREATE ROLE "Musico";

-- ASIGNACIÓN DE PERMISOS --

GRANT ALL ON TABLE public."Canciones" TO "Administrador" WITH GRANT OPTION;

GRANT SELECT ON TABLE public."Canciones" TO "Musico";

GRANT SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Canciones" TO "Productor";

GRANT SELECT ON TABLE public."Canciones" TO "Organizador";

GRANT ALL ON TABLE public."Conciertos" TO "Administrador" WITH GRANT OPTION;

GRANT INSERT, SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Conciertos" TO "Organizador";

GRANT SELECT ON TABLE public."Conciertos" TO "Productor";

GRANT SELECT ON TABLE public."Conciertos" TO "Musico";

GRANT ALL ON TABLE public."Discos" TO "Administrador" WITH GRANT OPTION;

GRANT SELECT ON TABLE public."Discos" TO "Organizador";

GRANT INSERT, SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Discos" TO "Productor";

GRANT SELECT ON TABLE public."Discos" TO "Musico";

GRANT ALL ON TABLE public."Entradas" TO "Administrador" WITH GRANT OPTION;

GRANT INSERT, SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Entradas" TO "Organizador";

GRANT SELECT ON TABLE public."Entradas" TO "Productor";

GRANT ALL ON TABLE public."Grupo" TO "Administrador" WITH GRANT OPTION;

GRANT INSERT, SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Grupo" TO "Productor";

GRANT SELECT ON TABLE public."Grupo" TO "Organizador";

GRANT SELECT ON TABLE public."Grupo" TO "Musico";

GRANT ALL ON TABLE public."Grupos_Tocan_Conciertos" TO "Administrador" WITH GRANT OPTION;

GRANT INSERT, SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Grupos_Tocan_Conciertos" TO "Organizador";

GRANT INSERT, SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Grupos_Tocan_Conciertos" TO "Productor";

GRANT SELECT ON TABLE public."Grupos_Tocan_Conciertos" TO "Musico";

GRANT ALL ON TABLE public."Musicos" TO "Administrador" WITH GRANT OPTION;

GRANT INSERT, SELECT, UPDATE, DELETE, TRIGGER ON TABLE public."Musicos" TO "Productor";

GRANT SELECT ON TABLE public."Musicos" TO "Organizador";

GRANT SELECT, UPDATE, TRIGGER ON TABLE public."Musicos" TO "Musico";

-- CREACIÓN DE USUARIOS -- 

CREATE USER admin WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION;

GRANT "Administrador" TO admin WITH ADMIN OPTION;

CREATE USER musico1 WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;

GRANT "Musico" TO musico1;

CREATE USER organizador1 WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;

GRANT "Organizador" TO organizador1;

CREATE USER productor1 WITH
	LOGIN
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;

GRANT "Productor" TO productor1;

CREATE USER nombre1 WITH
	LOGIN
	PASSWORD 'nombre1'
	NOSUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1;

GRANT "Musico" TO nombre1;

-- ROW LEVEL SECURITY --

ALTER TABLE "Musicos" ENABLE ROW LEVEL SECURITY;

CREATE POLICY admin_todo ON "Musicos" TO "Administrador"
	USING (true) WITH CHECK (true);

CREATE POLICY productor_todo ON "Musicos" TO "Productor"
	USING (true) WITH CHECK (true);

CREATE POLICY organizador_lectura ON "Musicos" 
	FOR SELECT TO "Organizador" 
	USING(true);

CREATE POLICY musicos_propio ON "Musicos" TO "Musico"
	USING(current_user = "Nombre");