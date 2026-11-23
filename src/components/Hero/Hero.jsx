import { useEffect, useState } from "react";
import { getStandings } from "../../services/teamsService";
import "./Hero.css";



function Hero() {
  const [primerPuesto, setPrimerPuesto] = useState(null);

  useEffect(() => {
  getStandings(2026)
    .then((data) => {
      setPrimerPuesto(data[0] ?? null);
    })
    .catch((err) => {
      console.error(err);
    });
}, []);

  return (
    <section className="hero">
      <h2>⚔️ Finalísima</h2>

      <div className="finalisima">
        <article className="finalisima__equipo">
          <span>1.º puesto</span>
          <strong>
            {primerPuesto ? primerPuesto.name : "Cargando..."}
          </strong>
        </article>

        <article className="finalisima__equipo">
          <span>Playoffs</span>
          <strong>Por definir</strong>
        </article>
      </div>
    </section>
  );
}

export default Hero;
