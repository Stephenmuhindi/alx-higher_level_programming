$(document).ready(function () {
	$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
		var movies = data.results;
		var listMovies = $("#list_movies");
		$.each(movies, function (index, movie) {
			var movieTitle = movie.title;
			var listItem = $("<li>").text(movieTitle);
			listMovies.append(listItem);
		});
	});
});
