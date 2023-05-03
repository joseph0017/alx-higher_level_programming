const l = window.$;

l.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (result) => {
    l.each(result, (i, getMovies) => {
      for (const k in getMovies) {
        l('#list_movies').append('<li>' + getMovies[k].title + '</li>');
      }
    });
  }

});
