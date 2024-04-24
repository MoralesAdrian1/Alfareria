# Alfareria
-----------------------------------------------------------------------------------------------------------------
# Descripcción
Se Llevar a cabo una automatización del sistema de iluminación en una alfareria de la localidad,
a través del uso de software y hardware e implementando sesnores y actuadores para llevar a cabo dicha 
automatización.
-----------------------------------------------------------------------------------------------------------------
# Objetivo
El Objetivo de esta automatización es ahorrar tiempo al personal de esta alfareria y al mismo tiempo mejorando
el consumo de energia y reduciendo los costes implementando el uso de sensores concetados a actuadores, ademas
de un registro en base de datos con un alaisís  sobre estos mismos permitiendo tomar decisiones en base a los 
datos ademas de permitir al usuario tener en su dispositivo movil un panel el cual le permita manejar todo su
sistema de luces desde la comodidad de su casa a través de un aplicativo de node-red con conexión a los
actuadores mediante la red local y una RaspBerry.
-----------------------------------------------------------------------------------------------------------------
# Software 
| Nombre de Software | Versión | Tipo |
|-|-|-|
|Thony|Versión más Reciente|Interprete de Código|
|Postgres|Versión más Reciente|Base de Datos SQL|
|Grafana|Versión más Reciente|Monitoreo de Datos|
|Node-red|Versión más Reciente|Conexión a internet|
-----------------------------------------------------------------------------------------------------------------
# Hardware 
| Nombre de Software | Tipo | Precio | Cantidad | Imagen |
|-|-|-|-|-|
|Rasberry Pi 4|Mono Ordenador|$1400|1|![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/692ff05a-0b83-457c-b215-414e81dd1cbd)|
|Esp32|Micro Controlador|$140|3|![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/b7e1fd13-9b82-4458-bc98-54ecef08fece)|
|Relé|Actuador|$45 c/u|2|![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/cfcab6a1-43e8-4262-a57c-095491fd21cb)|
|Modulo de 4 Relés|Actuador|$95 c/u|1|![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/209b5ffc-e233-45e0-8a8f-134aab699ccc)|
|Sensor Magnetico|Sensor|$35 c/u|1|![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/6205c71c-05c0-4f85-9197-b5133c8972e5)|
|Sensor Ultrasonico hc-sr04|Sensor|$89 c/u|1|![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/f89c9b9a-974b-41df-96bf-4b2d5d9c1dfb)|
|Cables Dupont|Cables|120|$119|1|![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/f1867c7b-355f-4386-bf44-75986f0ae487)|
-----------------------------------------------------------------------------------------------------------------
# Dasboard Node-red

![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/5e1df317-d472-4b85-b5eb-5d5769c68f1f)
![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/d92a5942-b525-439d-aa07-cbfff3d73c28)
![image](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/d7d8dc02-cda5-40e7-84bc-abd87077ec41)

-----------------------------------------------------------------------------------------------------------------
# Tablas de Postgres

Tabla sensor_type(En esta tabla podemos insertar el tipo de sensor "Analogico" o "Digital")
Código:
CREATE TABLE sensor_type (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, record_at TIMESTAMP DEFAULT now());

![Imagen de WhatsApp 2024-04-24 a las 17 32 08_6fe01408](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/64f3f5eb-7d7d-491c-916d-4f74b3053408)
********************************************************************************************


Sensors(En esta Tabla estan Almacenados Los datos de todos los sensores y actuadores)
Código:
CREATE TABLE sensor(id SERIAL PRIMARY KEY, type INTEGER, name VARCHAR(50), record_at TIMESTAMP DEFAULT now(), FOREIGN KEY(type) REFERENCES sensor_type(id));


![Imagen de WhatsApp 2024-04-24 a las 17 18 03_62153d0a](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/242c57df-5165-48ef-aaf8-b137e404b687)
********************************************************************************************
User(en esta tabla se almacenan los datos de los usuarios, los cuales podran insertar nuevos sensores ademas de 
permitir llevar un control sobre los datos que se ingresen desde node-red)
Código:
CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR(40), password VARCHAR(40), record_at TIMESTAMP DEFAULT now());

![Imagen de WhatsApp 2024-04-24 a las 17 18 03_25178140](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/51bfe2d1-69ef-466d-87a5-e5a6c8cac7ee)
********************************************************************************************
Alfareria(En esta Tabla Llegan todos los valores que mandan los sensores colocados en nustro proyecto seguido de 
el id de sensor y el id del usuario que esta enviando los datos)
Código:
CREATE TABLE Alfareria(id SERIAL PRIMARY KEY, sensor_id INTEGER, user_id INTEGER, value FLOAT, record_at TIMESTAMP DEFAULT now(), FOREIGN KEY(sensor_id) REFERENCES sensor(id), FOREIGN KEY(user_id) REFERENCES users(id));

![Imagen de WhatsApp 2024-04-24 a las 17 13 49_5646d1f3](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/3655ec5d-ee3b-4698-9f63-920d96468109)
![Imagen de WhatsApp 2024-04-24 a las 17 13 49_5ab500e3](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/88531a08-10a4-4d6c-afca-a7e6aec31cfe)
********************************************************************************************

-----------------------------------------------------------------------------------------------------------------
# Videos(Link a Carpeta de Drive)
En esta carpeta de drive se encuentran los videos de evidencia de funcionamiento y explicación del proyecto
ademas del video del Propietario de la empresa

https://drive.google.com/drive/folders/1hHm3X50f2-vqSjWN0Jp-R4MGt9V4pwWT?usp=drive_link

-----------------------------------------------------------------------------------------------------------------
#carta de Agradecimiento
![Imagen de WhatsApp 2024-04-24 a las 15 20 15_fdcfd827](https://github.com/MoralesAdrian1/Alfareria/assets/135056297/609302e6-8070-4ca2-9348-bb5e95b3ae76)

-----------------------------------------------------------------------------------------------------------------

