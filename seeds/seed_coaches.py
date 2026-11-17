from app.database import SessionLocal
from entities.coach import Coach

db = SessionLocal()

coaches = [
    Coach(id_coach=27804032, name="PAVINO OSCAR"),
    Coach(id_coach=29728013, name="BENAVIDEZ MATIAS"),
    Coach(id_coach=24384068, name="MENA CARLOS"),
    Coach(id_coach=17568723, name="MAIDANA OMAR"),
    Coach(id_coach=10921983, name="NADER EDGARDO"),
    Coach(id_coach=26763358, name="OLIVERA MARCELO"),
    Coach(id_coach=27826947, name="BERTERRECHE GUSTAVO"),
    Coach(id_coach=27461240, name="GIL LUCIANO"),
    Coach(id_coach=29909556, name="RODRIGUEZ SEBASTIAN"),
    Coach(id_coach=36386029, name="OLMOS CARLOS"),
    Coach(id_coach=22487733, name="SOTELO GERMAN"),
    Coach(id_coach=29303884, name="MOYANO MARTIN"),
]

db.add_all(coaches)
db.commit()
db.close()

print("Coaches cargados correctamente.")