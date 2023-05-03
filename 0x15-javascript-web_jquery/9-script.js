const l = window.$;

l.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: (result) => {
    l.each(result, (i, getWord) => {
      l('#hello').text(getWord.hello);
    });
  }
});
