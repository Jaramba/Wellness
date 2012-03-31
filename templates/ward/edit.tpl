{extends "base.tpl"}

{block "page-title"}Ward Management{/block}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>{if $ward->id}Edit{else}Add{/if} Ward</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="ward[type]" value="ward" />
				    	<div class="clearfix">
							<label >Name:</label>
							<div class="input">
								<input type="text" name="ward[name]" value="{$ward->name}" class="required" style="float: left"/>
							</div>
						</div>
						<div class="clearfix">
							<label >Location:</label>
							<div class="input">
								<input type="text" name="ward[location]" value="{$ward->location}" class="required" style="float: left"/>
							</div>
						</div>
						<div class="clearfix">
							<label >Description:</label>
							<div class="input">
								<textarea type="text" name="ward[notes]" class="required" style="float: left">{$ward->notes}</textarea>
							</div>
						</div>
						<div class="clearfix grey-highlight">
							<div class="input no-label">
					        	<input type="submit" class="button blue" value="Save">
					        </div>
					    </div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/block}