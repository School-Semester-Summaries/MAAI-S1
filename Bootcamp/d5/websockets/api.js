const WS_URL = "ws://localhost:8765";

const statusEl = document.getElementById("status");
const form     = document.getElementById("form");
const sendBtn  = document.getElementById("send");

const k1 = document.getElementById("k1");
const v1 = document.getElementById("v1");
const k2 = document.getElementById("k2");
const v2 = document.getElementById("v2");
const sent = document.getElementById("sent");
const resp = document.getElementById("resp");

let ws;

function setStatus(ok) {
  statusEl.textContent = ok ? "Connected" : "Disconnected";
  sendBtn.disabled = !ok;
}

function connect() {
  if (ws && (ws.readyState === WebSocket.OPEN || ws.readyState === WebSocket.CONNECTING)) return;
  ws = new WebSocket(WS_URL);
  ws.addEventListener("open",  () => setStatus(true));
  ws.addEventListener("close", () => setStatus(false));
  ws.addEventListener("error", () => setStatus(false));
  ws.addEventListener("message", e => {
    try { resp.textContent = JSON.stringify(JSON.parse(e.data), null, 2); }
    catch { resp.textContent = e.data; }
  });
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  if (!ws || ws.readyState !== WebSocket.OPEN) return;

  const a = k1.value.trim(), b = k2.value.trim();
  if (!a || !b) {
    resp.textContent = JSON.stringify({ status:"client_error", message:"Provide valid keys." }, null, 2);
    return;
  }
  const payload = { [a]: v1.value, [b]: v2.value };
  const text = JSON.stringify(payload);
  sent.textContent = JSON.stringify(payload, null, 2);
  ws.send(text);
});

document.addEventListener("DOMContentLoaded", connect);
