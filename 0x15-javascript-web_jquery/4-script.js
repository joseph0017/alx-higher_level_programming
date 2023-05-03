const toggleColors = window.$;

toggleColors('#toggle_header').click(() => {
  toggleColors('header').toggleClass('green red');
});
