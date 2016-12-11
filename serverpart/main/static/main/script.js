
function ModalInput() {
    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];
        modal.style.display = "block";
        modal.style.zIndex = 10;

// When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
        modal.style.zIndex = 0;
    }

// When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            modal.style.zIndex = 0;
        }
    }

}
function Modal() {
    $('#visitRoomFloor').click(ModalInput);
}