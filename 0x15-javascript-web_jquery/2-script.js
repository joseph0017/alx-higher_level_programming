const changeColor = window.$;

changeColor('#red_header').click(() => {
  changeColor('header').css('color', '#FF0000');
});
