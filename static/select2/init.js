function Select2AjaxTags(element, url) {
	$(element).select2({
		minimumInputLength: 1,
		maximumInputLength: 10,
		separator: ",",
		tags: true,
		ajax: {
			url: url,
			dataType: "json",
			data: function(term) {
				return {
					q: term
				};
			},
			results: function(data) {
				return {
					results: data.results
				};
			}
		}, 
	})
};

function SelectingEve(element, url, table) {
	$(element).on("select2-selecting", function(e){
        $.ajax({
	        type: "GET",
	        url: url+"?q="+e.val,
	        dataType: "json",
	        success:function(data) {
	        	for (var i=0; i<data.results.length; i++){
					$(table).dataTable().fnAddData([
		              	data.results[i].name,
		              	data.results[i].manager,
		              	data.results[i].phone,
		              	data.results[i].location,
		              	data.results[i].brand,
		              	data.results[i].category,
		              	"<a href=\"/company/"+data.results[i].id+"\" target=\"_blank\">详情 <i class=\"fa fa-eye\"></i></a>"
		            ]);
				}
	            
          	}
        });
    })
};