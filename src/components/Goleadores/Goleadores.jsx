import { useEffect, useState } from "react";
import "./Goleadores.css";
import { getScorers } from "../../services/playersService";

function Goleadores({ temporada }) {
  const [goleadores, setGoleadores] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setCargando(true);
    setError(null);

    getScorers(temporada)
      .then((data) => setGoleadores(data))
      .catch((err) => setError(err.message))
      .finally(() => setCargando(false));
  }, [temporada]);

  if (cargando) {
    return <p>Cargando goleadores...</p>;
  }

  if (error) {
    return <p>Error al cargar goleadores: {error}</p>;
  }

  if (goleadores.length === 0) {
    return <p>No hay goleadores registrados.</p>;
  }
  const maxGoles = goleadores[0].goals;

  const lideres = goleadores.filter(
    (jugador) => jugador.goals === maxGoles
  );
  const goleadoresConPosicion = goleadores.map((jugador) => {

  const posicion =
    goleadores.filter(
      (otro) => otro.goals > jugador.goals
    ).length + 1;

  return {
    ...jugador,
    posicion,
  };
});
  const lider = goleadores[0];

  return (
    <div className="goleadores">
      

      <div className="tabla-goleadores">
        {goleadoresConPosicion.map((jugador) => (
          <article
            key={jugador.id}
            className={`fila-goleador ${
            jugador.goals === maxGoles
            ? "fila-goleador--lider"
            : ""
            }`}
            >
            <span>{jugador.posicion}°</span>
            <strong>{jugador.name}</strong>
            <span>{jugador.position}</span>
            <b>{jugador.goals} goles</b>
          </article>
        ))}
      </div>
    </div>
  );
}

export default Goleadores;