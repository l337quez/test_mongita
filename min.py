import os
from mongita import MongitaClientDisk

base_dir = os.path.dirname(os.path.abspath(__file__))
storage_path = os.path.join(base_dir, "data_mongita")

client = MongitaClientDisk(storage_path)
db = client["mi_prueba_db"]
collection = db["proyectos"]

proyecto = {
    "nombre": "Proyecto local",
    "descripcion": "Guardado en carpeta del proyecto",
    "info": {"estado": "activo"}
}
insert_result = collection.insert_one(proyecto)
print("ID insertado:", insert_result.inserted_id)

print("Documentos:")
for doc in collection.find():
    print(doc)
