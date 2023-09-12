const onImageClick = (movieObj) => {
  const detailsDiv = document.getElementById("conteudo-direito");
  const defaultMessage = document.getElementById("msg-direito");

  defaultMessage.hidden = true;
  detailsDiv.style = "display: block;";

  const [title] = detailsDiv.querySelectorAll("#visualiza-titulo");
  const [image] = detailsDiv.querySelectorAll("#visualiza-imagem");
  const [releaseYear] = detailsDiv.querySelectorAll("#visualiza-ano-diretor");
  const [synopsis] = detailsDiv.querySelectorAll("#visualiza-sinopse");

  title.innerText = movieObj.title;
  image.src = `images/filmes/${movieObj.image}`;
  releaseYear.innerText = movieObj.releaseYear;
  synopsis.innerText = movieObj.synopsis;
};

const build = () => {
  const ajax = new XMLHttpRequest();

  ajax.onload = () => { console.log("Hello debug") }

  ajax.onreadystatechange = () => {
    if (ajax.readyState === 4 && ajax.status === 200) {
      try {
        const response = JSON.parse(ajax.response);

        if (typeof response !== "object") {
          console.error(
            "Os dados fornecidos não são objetos! Corrija e recarregue a página!"
          );
          return;
        }

        const data = new Array(...response);

        data.map((x, idx) => {
          const div = document.getElementById(`filme${++idx}`);
          div.onclick = () => {
            onImageClick(x);
          };

          const [image] = div.querySelectorAll("img");
          const [title] = div.querySelectorAll(".titulo");
          const [director] = div.querySelectorAll(".diretor");
          const [releaseYear] = div.querySelectorAll(".ano");
          const [synopsis] = div.querySelectorAll(".sinopse");

          image.src = `images/filmes/${x.image}`;
          title.innerText = x.title;
          director.innerText = x.director;
          releaseYear.innerText = x.releaseYear;
          synopsis.innerText = x.synopsis;
        });
      } catch (error) {
        console.error(`Erro! ${error}`);
      }
    }
  };

  ajax.onerror = () => {
    console.error(ajax.statusText);
  };

  ajax.open("GET", "{% static 'usipav/json/filmes.json'%}", true);
  ajax.send();
};
