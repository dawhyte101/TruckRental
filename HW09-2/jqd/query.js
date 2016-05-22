function performSearch() {
    var query = jQuery("#query-input").val();
    var params = {
                    q : query,
                    format : "json",
                    pretty : 1
                 };

    jQuery.ajax({
        url : "http://api.duckduckgo.com/",
        data : params,
        dataType : "jsonp",
        success : function(data) {
            jQuery("#results-header").html(data["Heading"]);
            jQuery("#results-content").html(data["AbstractText"] + data["Definition"]);
        }
    });
}

function establishHooks() {
   jQuery("#search-button").click(performSearch);
}

jQuery(document).ready(establishHooks);

