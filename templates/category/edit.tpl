{extends "base.tpl"}

{block "page-title"}Product Category: Admin{/block}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Product Category</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="category[type]" value="category" />
						<div class="clearfix">
							<label for="text_field">Name:</label>
							<div class="input">
								<input type="text" class="required" name="category[name]" value="{$category->name}" style="float:left"/>
							</div>
						</div>
						<div class="clearfix grey-highlight">
							<div class="input no-label">
						        <input type="submit" name="button blue" value="Save">
							</div>
					    </div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/block}