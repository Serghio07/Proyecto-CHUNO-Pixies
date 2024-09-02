document.getElementById('crearConferenciaForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

    // Capturar los datos del formulario
    let titulo = document.getElementById('titulo').value;
    let descripcion = document.getElementById('descripcion').value;
    let fecha = document.getElementById('fecha').value;

    // Realizar la solicitud AJAX
    fetch('/conferencias', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ titulo: titulo, descripcion: descripcion, fecha: fecha })
    })
    .then(response => response.json())
    .then(data => {
        // Mostrar la respuesta del servidor en el contenedor de respuesta
        document.getElementById('respuesta').innerText = data.mensaje;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('respuesta').innerText = 'Hubo un error al crear la conferencia.';
    });
});
