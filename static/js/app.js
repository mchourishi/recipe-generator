document.getElementById("get-recipe-btn").addEventListener("click", () => {
  fetch("/random")
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        document.getElementById("recipe").innerHTML = `<p>${data.error}</p>`;
      } else {
        document.getElementById("recipe").innerHTML = `
                    <h2>${data.name}</h2>
                    <p><strong>Ingredients:</strong> ${data.ingredients}</p>
                    <p><strong>Instructions:</strong> ${data.instructions}</p>
                    <p><strong>Cuisine:</strong> ${data.cuisine}</p>
                    <p><strong>Meal Type:</strong> ${data.meal_type}</p>
                `;
      }
    });
});

document.getElementById("search-btn").addEventListener("click", () => {
  const query = document.getElementById("search-box").value;
  fetch(`/search?query=${query}`)
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        document.getElementById(
          "search-results"
        ).innerHTML = `<p>${data.error}</p>`;
      } else {
        let results = "<ul>";
        data.forEach((recipe) => {
          results += `<li>${recipe.name} (${recipe.cuisine}, ${recipe.meal_type})</li>`;
        });
        results += "</ul>";
        document.getElementById("search-results").innerHTML = results;
      }
    });
});
