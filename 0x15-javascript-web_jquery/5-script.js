const add = window.$;

add('#add_item').click(() => {
  // to use the append method flip it like this
  // add('ul.my_list').appendTo('<li>Item</li>');
  add('<li>Item</li>').appendTo('ul.my_list');
});
