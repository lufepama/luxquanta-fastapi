PRUEBA TÉCNICA LUXQUANTA
Autor: Luis Felipe

- Levantar el servidor:
  $ docker compose up

- Correr los tests
  (1) Acceder a la terminal del contenedor levantado.
  $ docker exec -it {container_id} sh
  (2) Ejecuta el comando de pytest
  $ pytest test_main.py

NOTA:
La imagen coverage_image.png muestra el porcentaje coverage de los tests.
