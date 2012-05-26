$(function() {
	$('#create-question').click(function() {
		$('#create-question-modal').modal({
			onShow : function(dlg) {
				$(dlg.container).css('height', 'auto')
			}
		});
		return false;
	});
	$('#site_select').click(function(e) {
		e.preventDefault();
		$('#sites_menu').fadeToggle('fast');
		if($(this).text() == '▼ Switch Company') {
			$(this).text('▲ Switch Company');
		} else {
			$(this).text('▼ Switch Company');
		}
	});
	$('#interview_add').click(function(e) {
		e.preventDefault();
		$('#interview_menu').fadeToggle('fast');
	});
});
