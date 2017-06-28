document.addEventListener("DOMContentLoaded", function() {
  initProductsEvents();
});

function initProductsEvents() {
  $('.product_home').click(function() {
    var img = $(this).find('img');
    var src = img.attr('src');
    var body = $('body');
    var container = $('<div class="full-screen"></div>');
    var imgElement = $('<img src="' + src + '">');
    container.append(imgElement);
    container.hide().appendTo(body).fadeIn('normal');

    body.addClass('modal-open');
    $('.full-screen').click(closeModal);
  });

  $(document).keyup(function(e) {
    // On escape click
    if (e.keyCode == 27) {
      closeModal();
    }
  });
}

function closeModal() {
  $('.full-screen').fadeOut('normal', function() {
    $(this).remove();
  });
  $('body').removeClass('modal-open');
}
