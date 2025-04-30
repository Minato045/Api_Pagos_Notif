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
// Nuevas opciones para personalizar el PDF
const [includeLogo, setIncludeLogo] = useState(true);
const [includePaymentDetails, setIncludePaymentDetails] = useState(true);
const [includeUserInfo, setIncludeUserInfo] = useState(false);
const [includeTimestamp, setIncludeTimestamp] = useState(true);
const [footerMessage, setFooterMessage] = useState("Gracias por su pago");
const [contacto, setContacto] = useState(''); // Nuevo estado para el dato adicional


  useEffect(() => {
    document.body.className = tema; // actualiza el body con la clase del tema
  }, [tema]);

// Función para alternar el tema
const toggleTema = () => {
  setTema(prevTema => (prevTema === 'claro' ? 'oscuro' : 'claro'));
};

const handleSubmit = async (e) => {
  e.preventDefault();

  try {
    const body = {
      tipo_pago: tipoPago,
      canal: canal,
      tema: tema,
      monto: monto,
      contacto: contacto // Cambiar "contacto" a "to_phone"
    };

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

  const handleGenerateReport = async () => {
    const body = {
      tipo: tipoPago,
      monto: monto,
      includeLogo: includeLogo,
      title: "Reporte de Pago",
      includePaymentDetails: includePaymentDetails,
      includeUserInfo: includeUserInfo,
      theme: tema === "oscuro" ? "DARK" : "LIGHT",
      includeTimestamp: includeTimestamp,
      footerMessage: footerMessage,
      format: "A4",
    };
  
    try {
      const response = await fetch('http://localhost:5006/generar_reporte_pago', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });
  
      if (!response.ok) {
        throw new Error('Error al generar el reporte');
      }
  
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'reporte_pago.pdf';
      a.click();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      toast.error('❌ Error al generar el reporte');
    }
  };

  return (
    <div className="app-container">
      <img src="/logo.png" alt="Logo" className="logo" />
      <h1>Simulador de Pagos</h1>

      <button onClick={toggleTema} className="toggle-tema-btn">
        Cambiar a {tema === 'claro' ? 'Oscuro' : 'Claro'}
      </button>

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

        {/* Campo adicional según el canal seleccionado */}
        {canal === 'email' && (
          <label>
            Correo electrónico:
            <input
              type="email"
              value={contacto}
              onChange={e => setContacto(e.target.value)}
              placeholder="usuario@ejemplo.com"
              required
            />
          </label>
        )}
        {(canal === 'sms' || canal === 'whatsapp') && (
          <label>
            Número de teléfono:
            <input
              type="tel"
              value={contacto}
              onChange={e => setContacto(e.target.value)}
              placeholder="+1234567890"
              required
            />
          </label>
        )}
                <label>
                  Monto:
                  <input type="number" value={monto} onChange={e => setMonto(e.target.value)} />
        </label>

        {/* Nuevos controles para personalizar el PDF */}
        <label>
          <input
            type="checkbox"
            checked={includeLogo}
            onChange={e => setIncludeLogo(e.target.checked)}
          />
          Incluir Logo
        </label>

        <label>
          <input
            type="checkbox"
            checked={includePaymentDetails}
            onChange={e => setIncludePaymentDetails(e.target.checked)}
          />
          Incluir Detalles del Pago
        </label>

        <label>
          <input
            type="checkbox"
            checked={includePaymentDetails}
            onChange={e => setIncludePaymentDetails(e.target.checked)}
          />
          Incluir Detalles del Pago
        </label>

        <label>
          <input
            type="checkbox"
            checked={includeUserInfo}
            onChange={e => setIncludeUserInfo(e.target.checked)}
          />
          Incluir Información del Usuario
        </label>

        <label>
          <input
            type="checkbox"
            checked={includeTimestamp}
            onChange={e => setIncludeTimestamp(e.target.checked)}
          />
          Incluir Fecha y Hora
        </label>

        <label>
          Mensaje en el Pie:
          <input
            type="text"
            value={footerMessage}
            onChange={e => setFooterMessage(e.target.value)}
          />
          <button type="button" onClick={handleGenerateReport}>Generar Reporte PDF</button> 
          <button type="submit">Enviar</button>
        </label>
        </form>
        <hr/>
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
  };

  export default App; 