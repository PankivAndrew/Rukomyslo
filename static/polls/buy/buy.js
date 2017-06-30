var currentStep = 0;

document.addEventListener('DOMContentLoaded', function() {
  goToStep(currentStep);
  $('.buy-item .overlay span').click(deleteItem);
});

function goToStep(stepIndex) {
  var steps = $('.step');
  currentStep = stepIndex;
  var step;
  for (var i = 0; i < steps.length; i++) {
    step = steps[i];
    if (i == currentStep) {
      $(step).find('.step-content').first().show('normal');
    } else {
      $(step).find('.step-content').first().hide('normal');
    }
  }
}

function nextStep() {
  goToStep(currentStep + 1);
}

function deleteItem(ev) {
  var target = $(ev.target);
  var parentEl = target.closest('.buy-item');
  parentEl.remove();
}
