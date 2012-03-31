{extends "base.tpl"}

{block "page-title"}Drug Feedback: Doctor{/block}


{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Product Feedback</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="feedback[type]" value="feedback" />
						<div class="clearfix">
							<label for="text_field">Reason:</label>
							<div class="input">
								<textarea type="text" name="feedback[description]"/></textarea>
							</div>
						</div>
						<div class="clearfix grey-highlight">
							<div class="input">
					        	<input type="submit" name="button blue" id="" value="Save">
					        </div>
					    </div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/block}