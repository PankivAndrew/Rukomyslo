document.addEventListener("DOMContentLoaded", function() {
  initAffix();
  initDraggable();
  // Ya yebu;
  // $(window).resize(function() {
  //   initAffix();
  // });
});

function initAffix() {
  $('.prod-background').affix({offset: {bottom: getBottomOffset()} });
  // 49 is card container top padding
  $('.cart-container').affix({offset: {bottom: getBottomOffset() + 49} });
}

function initDraggable() {
  $('.cart-container .cart-item').on('dragend', function(event) {
    var target = $(this)
    var elementWidth = target.outerWidth();
    var movedHorizontally = event.offsetX;
    if(movedHorizontally > elementWidth) {
      event.preventDefault();
      $(this).remove();
      // You can add handling callback here (To call API e.g.)
    }
  });
}

function getBottomOffset() {
  var footerHeight = $('.footer').outerHeight();
  return footerHeight
}

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
   ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  var selector = '#' + data;
  var el = $(selector);
  var imgSrc = el.find('img').attr('src');
  var productName = el.find('.product-name').text();
  var productPrice = el.find('.product-price').text();
  var html = '<div class="cart-item" draggable="true">' +
                '<img src="' + imgSrc + '" alt="">' +
                '<span>' + productName + '</span>' +
                '<span>' + productPrice + '</span>' +
              '</div>';
  var newEl = $(html);
  $('.cart').append(newEl);
  initDraggable();

}
