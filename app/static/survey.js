// initializes page, setting event listeners to each button
// and activates highlight for selected buttons
function add_event_listeners() {
	var answer_buttons = document.getElementsByClassName('answer-button');
	for (button of answer_buttons) {
		button.addEventListener("click", function(ev) {
//  			ev.preventDefault();
  			let buttons_in_group = this.parentNode.children;
  			for (current_button of buttons_in_group) {
  				current_button.classList.remove("active");
  			}
  			this.classList.add('active');
//  			console.log(this.getAttribute('name')+ ": " +this.value);
		});
	}
	document.getElementById('submit').addEventListener("click", function(ev) {
	    ev.preventDefault();
	    alert("You clicked submit")
//	    js function to get all answers
	});
}
add_event_listeners();

