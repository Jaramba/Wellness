{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Categories</h2>
				<div class="widget_inside drugs-search">
					{if $request->user->belongsToGroups('admin,pharmacist')}
						<div id="add" style="width:100%;clear:both"><a href="{#BASE_URL#}/product-categories/add/" class="button blue" style="float:right">Add Category</a></div>
					{/if}
					<br/>
					{if $categories}
						<table class="regular">
							<tr>
								<th>Id</th>
								<th>Name</th>
								<th>Actions</th>
							</tr>
							{foreach $categories as $category}
								<tr>	
									<td>{$category->id}</td>
									<td>{$category->name}</td>
									<td>
										<a href="{#BASE_URL#}/product-categories/{$category->id}/">View</a>
										{if $request->user->belongsToGroups('admin')}
											|
											<a href="{#BASE_URL#}/product-categories/{$category->id}/edit/">Edit</a>
										{/if}
									</td>
								</tr>
							{foreachelse}
								<tr><td colspan="2">No Categories Found</td></tr>
							{/foreach}
						</table>
					{else}
						No Categories Found
					{/if}
				</div>
			</div>
		</div>
	</div>
{/block}