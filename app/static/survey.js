// initializes page, setting event listeners to each button
// and activates highlight for selected buttons
function add_event_listeners() {
	var answer_buttons = document.getElementsByClassName('btn-outline-primary');
	for (button of answer_buttons) {
		button.addEventListener("click", function(ev) {
  			ev.preventDefault();
  			let buttons_in_group = this.parentNode.children;
  			for (current_button of buttons_in_group) {
  				current_button.classList.remove("active");
  			}
  			this.classList.add('active');
  			console.log(this.getAttribute('name')+ ": " +this.value);
		});
	}
	return
}
add_event_listeners();


//adds event listener to submit button, preventing default submit until user string has been made
//and collects user answer values as a string
function submit_button() {
    document.getElementById('save-answers').addEventListener("click", function(ev) {
            ev.preventDefault();
            let user_string = make_user_answer_string()
            document.getElementById('answers').value = user_string
            console.log('successful load')
    });
    return
}
submit_button()

// called on submit survey button
// creates string of all user's answers
function make_user_answer_string() {
    var answer_buttons = document.getElementsByClassName('btn-outline-primary');
    var user_answer_array = [];
    for(var i=1; i<=answer_buttons.length; i++) {
        var currentQuestion = 'q'+i;
        try {
            var answer = check_responses(currentQuestion);
            user_answer_array.push(answer);
            currentQuestion = '';
        }
        catch(err) {
            console.log('caught')
        }
    }
    console.log(user_answer_array);
    array_as_string = user_answer_array.toString();
    return array_as_string
}


// returns (to make user answer string) which button was
// selected for each question
function check_responses(question_name) {
    var answer_buttons_of_question = document.getElementById(question_name).children;
    for (var j = 0; j < answer_buttons_of_question.length; j++) {
        if (answer_buttons_of_question[j].getAttribute('class') == 'btn btn-outline-primary active') {
            let the_value = answer_buttons_of_question[j].getAttribute('value');
            return the_value;
        }
    }
}