import React, { useState, useEffect } from 'react';
import './App.css';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const [tipoPago, setTipoPago] = useState('credit');
  const [canal, setCanal] = useState('email');
  const [tema, setTema] = useState('claro');
  const [monto, setMonto] = useState(100);
  const [htmlResponse, setHtmlResponse] = useState('');

  useEffect(() => {
    document.body.className = tema; // actualiza el body con la clase del tema
  }, [tema]);

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const body = {
      tipo_pago: tipoPago,
      canal: canal,
      tema: tema,
      monto: monto
    };
  
    try {
      const response = await fetch('http://localhost:5003/realizar_pago_y_notificar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });
  
      const html = await response.text();
      setHtmlResponse(html);
  
      // 🧼 Limpiar el HTML para quitar encabezado y pie de página
      const tempElement = document.createElement('div');
      tempElement.innerHTML = html;
  
      // Remover <header> y <footer>
      const header = tempElement.querySelector('header');
      const footer = tempElement.querySelector('footer');
      if (header) header.remove();
      if (footer) footer.remove();
  
      // ✅ Mostrar HTML estilizado en el toast
      toast(
        <div dangerouslySetInnerHTML={{ __html: tempElement.innerHTML }} />,
        {
          autoClose: 8000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          position: "top-right",
          theme: tema === 'oscuro' ? 'dark' : 'light',
        }
      );
  
    } catch (error) {
      toast.error('❌ Error al procesar el pago');
    }
  };  

  return (
    <div className="app-container">
      <img src="/logo.png" alt="Logo" className="logo" />
      <h1>Simulador de Pagos</h1>

      <form onSubmit={handleSubmit} className="formulario">
        <label>
          Tipo de pago:
          <select value={tipoPago} onChange={e => setTipoPago(e.target.value)}>
            <option value="credit">Tarjeta de Crédito</option>
            <option value="debit">Tarjeta Débito</option>
            <option value="paypal">PayPal</option>
          </select>
        </label>

        <label>
          Canal de notificación:
          <select value={canal} onChange={e => setCanal(e.target.value)}>
            <option value="email">Email</option>
            <option value="sms">SMS</option>
            <option value="push">Push</option>
            <option value="whatsapp">WhatsApp</option>
          </select>
        </label>

        <label>
          Tema visual:
          <select value={tema} onChange={e => setTema(e.target.value)}>
            <option value="claro">Claro</option>
            <option value="oscuro">Oscuro</option>
          </select>
        </label>

        <label>
          Monto:
          <input type="number" value={monto} onChange={e => setMonto(e.target.value)} />
        </label>

        <button type="submit">Enviar</button>
      </form>

      <hr />

      <h2>Respuesta del servidor:</h2>
      <div
        className="respuesta-servidor"
        dangerouslySetInnerHTML={{ __html: htmlResponse }}
      />

      {/* Componente ToastContainer 👇 */}
      <ToastContainer
        position="top-right"
        autoClose={9000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme={tema === 'oscuro' ? 'dark' : 'light'}
      />
    </div>
  );
}

export default App;
