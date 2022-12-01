async function getUserData() {
    const response = await fetch('/users');
    return response.json();
}

function loadTable(users) {
    const table = document.querySelector('#result');
    for (let user of users) {
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.email}</td>
        </tr>`;
    }
}

async function main() {
    const users = await getUserData();
    loadTable(users);
}


// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}





main();