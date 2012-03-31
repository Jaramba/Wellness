{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Ward Detail</h2>
				<div class="widget_inside drugs-search">
					<div class="form">
						<div class="clearfix">
							Id: {$ward->id}
						</div>
						<div class="clearfix">
							Name: {$ward->name}
						</div>
						<div class="clearfix">
							Location: {$ward->location}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/block}
