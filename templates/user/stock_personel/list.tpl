{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Stock Personel</h2>
				<div class="widget_inside drugs-search">
					{if $request->user->belongsToGroups('admin')}
						<div id="add" style="width:100%;clear:both"><a href="{#BASE_URL#}/admin/staff/stock-personel/add/" class="button blue" style="float:right">Add Stock Personel</a></div>
					{/if}
					{if $stock_personels}
						<table class='regular'>
							<tr>
								<th>Id</th>
								<th>First Name</th>
								<th>Last Name</th>
								<th>Actions</th>
							</tr>
							{foreach $stock_personels as $stock_personel}
								<tr>	
									<td>{$stock_personel->id}</td>
									<td>{$stock_personel->first_name}</td>
									<td>{$stock_personel->last_name}</td>
									<td>
										<a href="{#BASE_URL#}/stock_personel/{$stock_personel->id}/">View</a>
										{if $request->user->belongsToGroups('admin,pharmacist')}
											|
											<a href="{#BASE_URL#}/admin/staff/stock-personel/{$stock_personel->id}/edit/">Edit</a> |
											<a href="{#BASE_URL#}/admin/staff/stock-personel/{$stock_personel->id}/delete/">Delete</a>
										{/if}
									</td>
								</tr>
							{foreachelse}
								<tr><td colspan="2">No Stock Personel Found</td></tr>
							{/foreach}
						</table>
					{else}
						No Stock Personel Found
					{/if}
				</div>
			</div>
		</div>
	</div>
{/block}
