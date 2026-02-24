export function connectWebSocket(clientId, onMessage) {
  const socket = new WebSocket(`ws://localhost:8000/ws/${clientId}`);

  socket.onmessage = (event) => {
    onMessage(event.data);
  };

  return socket;
}
