function taskAction(action,id){
	jQuery.ajax({
		url:"tasks.php",
		type: "POST",
		data = "action="+action+"&id="+id,
		success: function(){},
		error: function(){}
	});
}