document.addEventListener('DOMContentLoaded', function() {
  
    document.querySelectorAll('#buysell').forEach(elem => {
        elem.addEventListener('click', function () {
            buyandsell(elem.parentNode);
            // alert(elem.parentNode.querySelector('.name').textContent);
        });
    })
    
  });

function buyandsell(elem) {
    fetch('/api/buysell', {
        method : 'POST',
        body : JSON.stringify({
            action: elem.querySelector('#buysell').value,
            amount: elem.querySelector('#formFileSm').value,
        })
    })
    .then(response => response.json())
}