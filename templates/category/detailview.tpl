{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Products</h2>
				<div class="widget_inside drugs-search">
					<p>
						Id: {$category->id}
					</p>
					<p>
						Name: {$category->name}
					</p>
				</div>
			</div>
		</div>
	</div>
{/block}