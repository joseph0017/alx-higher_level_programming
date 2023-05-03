const l = window.$;
const uri = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

const getData = (result) => {
  l('#character').text(result.name);
};

l.getJSON(uri, getData);
