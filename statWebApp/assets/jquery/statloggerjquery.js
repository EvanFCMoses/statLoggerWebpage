$(document).ready(function() {

	$("#sortMaladiesByName").click( function(event) {
		// alert('your message on click');
	});


	$('form#dataEntry').submit(function(){
		$(this).find(':input[type=submit]').prop('disabled',true);
	});

});