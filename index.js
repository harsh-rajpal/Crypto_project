var click = document.getElementById('clickme');
click.addEventListener('click', myfunction);

function myfunction() {
  var tablewrap = document.getElementById('displaytable');
  tablewrap.classList.toggle('hidden')
};
