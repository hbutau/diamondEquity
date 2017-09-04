jQuery(document).ready(function(){
	"use strict";
	jQuery('.inner-faq-panel-heading a').on('click',function(){
		var faq_status = '';
		faq_status = jQuery(this).attr('aria-expanded');
		if( faq_status == 'true' )
			jQuery(this).prev().attr("src", "images/plus-mark.png");
		if( faq_status == 'false' )
			jQuery(this).prev().attr("src", "images/minus-mark.png");
	});
	jQuery('.inner-faq-panel-heading img').on('click',function(){
		$(this).next().trigger("click");
	});				
	jQuery('.inner-faq-panel-heading a').first().trigger("click");				
});