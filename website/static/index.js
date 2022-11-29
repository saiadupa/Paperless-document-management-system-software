function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

function deleteEvents(EventsId) {
    fetch("/delete-Events", {
      method: "POST",
      body: JSON.stringify({ EventsId: EventsId }),
    }).then((_res) => {
      window.location.href = "/Events";
    });
  }
