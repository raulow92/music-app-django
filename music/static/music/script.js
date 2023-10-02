const MyApp = {
    initialize: () => {
        const artistForm = document.getElementById("artist-form");
        if (artistForm) {
            artistForm.addEventListener("submit", (event) => {
                event.preventDefault();
                MyApp.submitArtist(artistForm);
            });
        }

        // const pubDate = document.getElementById("id_pub_date");
        // if (pubDate) {
        //     pubDate.addEventListener("input", (event) => {
        //         const albumDate = new Date(event.target.value);
        //         const now = new Date();

        //         if (albumDate <= now) {
        //             console.log("El álbum es del pasado");
        //             event.target.setCustomValidity("");
        //         } else {
        //             console.log("El álbum es del futuro");
        //             event.target.setCustomValidity(
        //                 "La fecha del álbum no puede ser posterior a la fecha actual"
        //             );
        //         }
        //     });
        // }
    },
    submitArtist: (formElem) => {
        const name = document.getElementById("id_name").value;
        const genre = document.getElementById("id_genre").value;
        const artistId = formElem.dataset.artistId;

        fetch("http://127.0.0.1:8000/api/v1/artists/" + artistId + "/", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: name,
                genre: genre,
            }),
        }).then((response) => {
            if (response.status >= 200 && response.status < 300) {
                const alert = document.querySelector(".alert-success");
                const message = '<p class="alert-success">Datos guardados con éxito!</p>';
                alert?.remove();
                formElem.insertAdjacentHTML("beforeend", message);
                setTimeout(() => alert?.remove(), 3000);
            }
        });
    },
};

if (document.readyState === "loading") {
    document.addEventListener("readystatechange", (event) => {
        if (event.target.readyState === "interactive") {
            MyApp.initialize();
        }
    });
} else {
    MyApp.initialize();
}
