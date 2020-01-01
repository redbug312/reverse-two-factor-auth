$(document).ready(function() {
  $('.ui.form').form({
    inline: true,
    fields: {
      username: 'empty',
      password: ['empty', 'length[6]'],
      confirmed: 'match[password]',
      agreement: 'checked',
    }
  });
});
