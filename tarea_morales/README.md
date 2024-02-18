# mi-proyecto
Proyecto inicial del bootcamp de python


# Configuracion ambiente local desarrollo

1. Creación de ambiente virtual, utilizar el siguiente comando:
```python
python -m venv venv
```
2. Activar ambiente virtual, con el siguiente comando:
```bash
venv\Scripts\activate
```

3. Instalación dependencias
```python
pip install django
```

4. Creación proyecto inicial Django , solo si es la primera vez usar el siguiente comando:
```python
py -m django startproject jarana
```

5. Comprobar servidor, ejecutar el siguiente comando, dentro de la carpeta jarana:
```python
py manage.py runserver
```

**NOTA:** Abrir en el navegador la siguiente ruta `http://127.0.0.1:8000/`

# Configuracion aplicacion

**NOTA:** Cuando queremos crear una nueva aplicacion:
1. Crear aplicacion nueva
```python
py manage.py startapp nombre_app
```

```
jonathan_arana
|__fitness_app
|____models.py
|____urls.puy

```