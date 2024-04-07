btn = document.getElementsByClassName('header_btn');
num_inp = document.getElementsByClassName('num_inp');


document.getElementById('btn').addEventListener('click', function() {
    let buttonDiv = document.getElementById('btn');
    let divToShow = document.getElementById('num_inp');
  
    // Приховуємо кнопку
    buttonDiv.style.display = 'none';
    // Показуємо додатковий div
    divToShow.style.display = 'flex';
  });

