CREATE TABLE public.User (
	id varchar(50) NOT NULL,
	email varchar(50) NULL,
	"name" varchar(20) NULL,
	created_at date NULL,
	updated_at date NULL,
	CONSTRAINT User_email_key UNIQUE (email),
	CONSTRAINT User_pkey PRIMARY KEY (id)
);
CREATE TABLE public.Account (
	id serial4 NOT NULL,
	name varchar(50) NULL,
	currency varchar(5) NULL,
	user_id varchar(50) NOT NULL,
	CONSTRAINT Account_pkey PRIMARY KEY (id),
	CONSTRAINT Account_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.User(id)
);
CREATE TABLE public.Category (
	id serial4 NOT NULL,
	"name" varchar(20) NOT NULL,
	user_id varchar(50) NOT NULL,
	CONSTRAINT Category_pkey PRIMARY KEY (id),
	CONSTRAINT Category_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.User(id)
);
CREATE TABLE public.Transaction (
	id serial4 NOT NULL,
	amount int4 NOT NULL,
	category_id int4 NOT NULL,
	account_id int4 NOT NULL,
	user_id varchar(50) NOT NULL,
	description varchar(50) NULL,
	created_at date NULL,
	CONSTRAINT Transaction_pkey PRIMARY KEY (id),
	CONSTRAINT Transaction_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.Account(id),
	CONSTRAINT Transaction_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.Category(id),
	CONSTRAINT Transaction_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.User(id)
);
