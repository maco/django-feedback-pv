
var feedback = {};
feedback.init = function(config) {
    if (!(config.button && config.drop && config.popup))
        throw "invalid params";
    config.popup.find('form.feedback').ajaxForm({
        'beforeSubmit':function(){
            config.popup.addClass('loading');
		  return true;
        },
        'success':feedback.done(config),
		'error': feedback.error(config)
    });

    config.button.colorbox({inline: true, href:"#"+config.popup[0].id, width: 560, height: 450, transition: "none", onComplete: function() { config.popup.removeClass('thanks'); config.popup.find('input[name=email]').focus();} })
};

feedback.done = function(config) {
    return function(data) {
    	config.popup.find('.error').addClass("hiding");
    	data = eval('(' + data + ')');
    	if (data.error) {
    		config.popup.find('.general.error').removeClass("hiding").text(data.error);
    		return;
    	}
    	if (data.errors) {
    		for (var key in data.errors) {
    			config.popup.find('.error.' + key).removeClass("hiding").text(data.errors[key][0]);
    		}
    		return;
    	}
        config.popup.removeClass('loading');
        config.popup.addClass('thanks');
        config.popup.find('textarea').val('');
        config.popup.find('input[name=subject]').val('');
        config.popup.delay(3000).queue( function(){ $.colorbox.close(); });
    };
};
feedback.error = function(config) {
	return function (jqXHR, textStatus, errorThrown) {
        config.popup.find('.error.general').removeClass("hiding").text("There was a problem submitting your feedback.");
	};
};

