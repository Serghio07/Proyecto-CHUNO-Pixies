document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: [
            { title: 'Conferencia 1', start: '2024-09-15' },
            { title: 'Conferencia 2', start: '2024-09-18' },
            { title: 'Conferencia 3', start: '2024-09-22' }
        ]
    });
    calendar.render();
});

function addNote() {
    var noteText = document.getElementById('note-input').value;
    if (noteText !== "") {
        var note = document.createElement('div');
        note.className = 'note';
        note.textContent = noteText;
        document.getElementById('notes-container').appendChild(note);
        document.getElementById('note-input').value = ""; // Limpiar el textarea
    }
}
