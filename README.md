![Banner](./images/Banner%20copia.jpg)

- [SITIO WEB](https://juniortechtroopers.com.ar/)
- [YT](https://www.youtube.com/@JuniorTechTroopers)
- [Nelson Lassa](https://github.com/NelsonLassa) [Franco Pagano](https://github.com/PaganoFranco) [Yamil Yunes](https://github.com/yunesyamil) [Marianela Purretta](https://github.com/MarianelaPurretta) [Joaquín Viñolo](https://github.com/joaquin9830) [Mauro Barrosoo](https://github.com/Maujj1999) 

 ## JUNIOR TECH TROOPERS
<img src="./images/NELSONNNNNNNN.png?raw=true" width="49%" height="49%"> <img src="./images/FRA.png?raw=true" width="49%" height="49%">
<img src="./images/YAMILLLL.png?raw=true" width="49%" height="49%"> <img src="./images/marii.png?raw=true" width="49%" height="49%"> 
<img src="./images/JOACOOOO.png?raw=true" width="49%" height="49%"><img src="./images/mauuuu.png?raw=true" width="49%" height="49%">

# TROOPER STAY

**`Sistema de estadía`**

En esta aplicación se podrán publicar alojamientos con sus respectivas características. Estos alojamientos se almacenaran en una base de datos, permitiendo así mostrar estos y que los usuarios puedan hacer uso del servicio.

El usuario podrá iniciar sesión y registrarse en caso de no tener credenciales. Además, contará con un filtro que permitirá la búsqueda por localidad y fecha.

## **Descripción del Proyecto**

Aplicación Python que permite a los usuarios publicar y buscar alojamientos para estancias temporales. Los usuarios pueden registrarse, iniciar sesión y tener roles duales: publicar alojamientos o contratar servicios de alojamiento. La aplicación utiliza diferentes bases de datos MySQL para almacenar la información de los alojamientos y los usuarios.

## Requisitos

**`Lenguajes:`** 

- **Python** versión: 11 - 12
- **MySQL**

Visualización: **Tkinter**

## Funcionalidades:

## Principales utilidades

- **`Login`**
    
    El usuario deberá ingresar sus credenciales y estas serán verificadas mediante una consulta a la base de datos. Esto le permitirá ingresar a la aplicación y hacer uso de sus funciones - servicios.
    
    Este proceso implica los siguientes pasos:
    
    - **Ingreso de credenciales.**
    - **Validación de credenciales.**
    - **Acceso a funcionalidades.**
- **`Register`**
    
    Se utiliza para gestionar el proceso de registro de usuarios. Realizando validaciones de los datos ingresados por el usuario, como por ejemple el e-mail, corrigiéndolos en caso de ser necesario y luego los almacenándolos en la base de datos. 
    
- **`Base de datos`**
    
    La aplicación cuenta con dos bases de datos relacionales (MySQL) conectadas, creando así un sistema organizado para almacenar, gestionar y recuperar información de manera eficiente.
    
    Esto permite:
    
    - **Estructura organizada.**
    - **Acceso y recuperación de datos.**
    - **Gestión de datos.**
    - **Seguridad y control de acceso.**
    - **Integridad de datos.**
- **`Board Mind`**
    
    Este es el menú o tablero principal de la aplicación en la cual se mostrará los datos del usuario que inició sesión. 
    
    Además, en el se podrán visualizar diferentes opciones de selección (botones interactivos).
    
    - **Buscar.**
    - **Agregar.**
    - **Administrar.**
- **`User Data`**
    
    Datos del Usuario cargados en la Base de Datos:
    
    - **Id**
    - **Username**
    - **Password**
    - **Email**
    - **First_Name**
    - **Last_Name**
    - **Age**
    - **Phone**
    - **Cash**
- **`Look for`**
    
    A este punto los hospedajes ingresados por el usuario ya deben estar disponibles con los siguientes datos:
    
    - **Id**
    - **Id_Stay**
    - **Id_User_Owner**
    - **Id_User Renter**
    - **Start_Date**
    - **End_Date**
    - **Status**
    
- **`Filter`**
    
    Permite filtrar al cliente los hospedajes mediante dos apartados: p**rovincia,**  departamento y localidad y por fecha de entrada y salida.
    
- **`Search Result`**
    
    Traerá a pantalla los hospedajes disponibles de acuerdo al filtro y le permitirá al usuario seleccionar entre los alojamientos filtrados.
    
- **`Selection View`**
    
    Mostrará al usuario el hospedaje seleccionado y las características del mismo.
    
- **`Rental Creation`**
    
    Aquí el usuario podrá cargar hospedajes para su posterior alquiler con los datos:
    
    - **Id**
    - **Name**
    - **Location**
    - **Night_Price**
    - **Capacity**
    - **Type**
    - **Image**
- **`Rental Edit`**
    
    Aquí el usuario podrá editar los hospedajes que se asocien a su id

  ## Base de datos

- **Requisitos**
    
    Para facilitar la instalación de dependencias necesarias se creó un archivo llamado “requierement.txt”. El mismo instala todos los requisitos necesarios.
    
    - **Archivo**
        
        ```sql
        bcrypt==4.1.3
        
        tkcalendar~=1.6.1
        python-dotenv~=1.0.1
        mysql~=0.0.3
        mysql-connector-python~=8.4.0
        ```
        
    - **¿Para qué las dependencias?**
        
        Para conectar una base de datos **MySQL** a **python** es necesario instalar una dependencia llamada “mysql connector”.
        
        ¿Cómo lo realizamos?
        
        Desde una terminal utilizaremos el siguiente comando:
        
        ```sql
        **pip** install mysql-connector-python
        ```
        
        - **Variables de entorno**
            
            Es necesario crear un archivo .env para las credenciales:
            
            ```sql
            DB_HOST_1=localhost (host donde se encuentra la base de datos)
            DB_PORT_1=3306 (numero de puerto)
            DB_USER_1=tu_usuario
            DB_PASSWORD_1=tu_contraseña
            DB_NAME_1=nombre_de_base_de_datos
            
            DB_HOST_2=localhost (host donde se encuentra la base de datos)
            DB_PORT_2=3306 (numero de puerto)
            DB_USER_2=tu_usuario
            DB_PASSWORD_2=tu_contraseña
            DB_NAME_2=nombre_de_base_de_datos
            ```
            
            Debemos instalar dotenv (para hacer uso de estas credenciales) desde la terminal utilizando este código:
            
            ```sql
            pip install python-dotenv
            ```

La base de datos estará conformada por dos base de datos:

**`DB_USERS`**

**`DB_STAYS`**

Tendrán 6 tablas en total:

- **DB_USERS**
    - **Usuarios**
        
        ```sql
        Nombre del Campo	   Tipo de Dato	   Descripción
        user_id	                  INT	       **Identificador único del usuario**
        username	             VARCHAR(50)	 Nombre de usuario
        password	             VARCHAR(255)	 Contraseña del usuario (encriptada)
        firstname	             VARCHAR(50)	 Nombre del usuario
        lastname	             VARCHAR(50)	 Apellido del usuario
        email	                 VARCHAR(100)	 Correo electrónico del usuario
        birthdate	                DATE	     Fecha de nacimiento del usuario
        age	                       INT	     Edad del usuario
        phone	                 VARCHAR(20)	 Número de teléfono del usuario
        money	                DECIMAL(10, 2) Saldo de dinero del usuario
        active	                BOOLEAN	     Indica si el usuario está activo o no
        ```
        
- **DB_STAYS**
    - **Departamentos**
        
        ```sql
        Nombre del Campo	    Tipo de Dato	   Descripción
        provincia_id	            INT	         Identificador único de la provincia
        nombre	               VARCHAR(50)	    Nombre del departamento
        ```
        
    - **Hosting**
        
        ```sql
        Nombre del Campo	    Tipo de Dato	    Descripción
        hosting_id	              INT	          Identificador único del hosting
        owner_id	                INT	          Identificador del propietario del hosting
        name	                 VARCHAR(100)	    Nombre del hosting
        address	               VARCHAR(255)	    Dirección del hosting
        location_id	              INT	          Identificador de la ubicación
        capacity	                INT	          Capacidad del hosting
        daily_cost	              INT	          Costo diario de alojamiento
        state	                   TINYINT	      Estado del hosting (0: inactivo, 1: activo)
        ```
        
    - **Localidades**
        
        ```sql
        Nombre del Campo	     Tipo de Dato	   Descripción
        localidad_id	             INT	       Identificador único de la localidad
        departamento_id	           INT	       Identificador del departamento
        nombre	               VARCHAR(100)	   Nombre de la localidad
        ```
        
    - **Provincias**
        
        ```sql
        Nombre del Campo	     Tipo de Dato     	Descripción
        provincia_id	             INT	          Identificador único de la provincia
        nombre	               VARCHAR(100)	      Nombre de la provincia
        ```
        
    - **Rental_Register**
        
        ```sql
        Nombre del Campo	    Tipo de Dato	    Descripción
        rent_id	                  INT	          Identificador único del registro de alquiler
        locator_id	              INT	          Identificador del locador (arrendador)
        renter_id	                INT	          Identificador del arrendatario
        hosting_id	              INT	          Identificador del hosting
        start_date	              DATE	        Fecha de inicio del alquiler
        end_date	                DATE	        Fecha de fin del alquiler
        number_of_days	          INT	          Número de días de alquiler
        total_cost	              INT	          Costo total del alquiler
        ```


## **Estructura del Proyecto**


## **`ENCARPETADO`**

- **MVC**
    
    Utilizamos este patrón arquitectónio para la distribución, estructuración del proyecto, facilitando así la separación del mismo. 
    
    - **¿Qué es MVC?**
        
        MVC (**Model-View-Controller)** es un patrón arquitectónico ampliamente utilizado en el desarrollo de software, especialmente en aplicaciones web y GUI (interfaces gráficas de usuario). Su objetivo principal es separar las preocupaciones dentro de una aplicación, dividiéndola en tres componentes principales: el Modelo, la Vista y el Controlador. Cada uno de estos componentes tiene responsabilidades específicas, lo que promueve un diseño más estructurado, modular y fácil de mantener.
        
    - **Desglose del MVC:**
        1. **Modelo (Model):**
            - Representa los datos y la lógica empresarial de la aplicación.
            - Gestiona el acceso y la manipulación de los datos.
            - No depende de la interfaz de usuario ni de cómo se presentan los datos al usuario.
            - Puede incluir estructuras de datos, clases, lógica de validación, acceso a la base de datos, etc.
            - En términos simples, es el "núcleo" de la aplicación que gestiona el comportamiento de los datos.
        2. **Vista (View):**
            - Es responsable de la presentación de los datos al usuario y de la interfaz de usuario.
            - Recibe datos del Modelo y los muestra de manera que sea comprensible para el usuario final.
            - No realiza lógica de negocio ni manipula datos; simplemente muestra la información.
            - Puede ser una página web, una ventana de GUI, una plantilla HTML, etc.
        3. **Controlador (Controller):**
            - Actúa como intermediario entre el Modelo y la Vista.
            - Gestiona las interacciones del usuario y las solicitudes de entrada.
            - Interpreta las acciones del usuario (por ejemplo, clics de botón, entradas de formulario) y realiza las operaciones necesarias.
            - Actualiza el Modelo según las acciones del usuario y actualiza la Vista para reflejar los cambios en los datos.

- [DOCUMENTACIÓN COMPLETA](https://horn-sort-9a3.notion.site/Trooper-Stay-Python-f0ed33c37d5b4effadca2d79b7414b46)
  

