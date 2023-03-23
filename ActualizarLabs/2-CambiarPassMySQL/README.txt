1- Conocer el user de mysql almacenado en el fichero /etc/mysql/debian.cnf
user: debian-sys-maint
pass: 1Riyedz7K4kfJ8H3 

2- escribir en consola
mysql -u debian-sys-maint -p

cuando pida la contrasenna escribir la anterior

lo anterior te lleva a la consola de mysql

3- conocer los usuarios en el sistema
	>> select user from user;	 

Estando en la consola de mysql escribir los sgtes comandos para resetear el pass del user admin:
	>> use mysql;
	>> alter user 'admin'@'localhost' identified by 'admin';


