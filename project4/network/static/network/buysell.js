document.addEventListener('DOMContentLoaded', function() {
  
    document.querySelectorAll('#buysell').forEach(elem => {
        elem.addEventListener('click', function () {
            buyandsell(elem);
            // alert(elem.parentNode.querySelector('.name').textContent);
        });
    })
    
  });

function buyandsell(elem) {
    alert(elem.value);
    fetch('/api/buysell', {
        method : 'POST',
        body : JSON.stringify({
            action: elem.value,
        })
    })
    .then(response => response.json())
    .then(result => {
        // Print results
        console.log(result);
    })
}