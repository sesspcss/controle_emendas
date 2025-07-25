import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [emendas, setEmendas] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/emendas/").then(res => {
      setEmendas(res.data);
    });
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Lista de Emendas</h1>
      <ul className="space-y-2">
        {emendas.map((emenda) => (
          <li key={emenda.id} className="bg-white shadow p-4 rounded">
            <p><strong>Número:</strong> {emenda.numero}</p>
            <p><strong>Parlamentar:</strong> {emenda.parlamentar}</p>
            <p><strong>Status:</strong> {emenda.status}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

