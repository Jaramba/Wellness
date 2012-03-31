{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Nurses</h2>
				<div class="widget_inside drugs-search">
					{if $request->user->belongsToGroups('admin')}
						<div id="add" style="width:100%;clear:both"><a href="{#BASE_URL#}/admin/staff/nurses/add/" class="button blue" style="float:right">Add Nurse</a></div>
					{/if}
					{if $nurses}
						<table class='regular'>
							<tr>
								<th>Id</th>
								<th>First Name</th>
								<th>Last Name</th>
								<th>Actions</th>
							</tr>
							{foreach $nurses as $nurse}
								<tr>	
									<td>{$nurse->id}</td>
									<td>{$nurse->first_name}</td>
									<td>{$nurse->last_name}</td>
									<td>
										<a href="{#BASE_URL#}/nurse/{$nurse->id}/">View</a>
										{if $request->user->belongsToGroups('admin,pharmacist')}
											|
											<a href="{#BASE_URL#}/admin/staff/nurses/{$nurse->id}/edit/">Edit</a> |
											<a href="{#BASE_URL#}/admin/staff/nurses/{$nurse->id}/delete/">Delete</a>
										{/if}
									</td>
								</tr>
							{foreachelse}
								<tr><td colspan="2">No Nurses Found</td></tr>
							{/foreach}
						</table>
					{else}
						No Nurse Found
					{/if}
				</div>
			</div>
		</div>
	</div>
{/block}
