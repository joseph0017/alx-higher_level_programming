const changeColor = window.$;

changeColor('#red_header').click(() => {
  changeColor('header').addClass('red');
});
