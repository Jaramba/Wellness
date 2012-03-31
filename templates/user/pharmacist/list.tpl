{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Pharmacists</h2>
				<div class="widget_inside drugs-search">
					{if $request->user->belongsToGroups('admin')}
						<div id="add" style="width:100%;clear:both"><a href="{#BASE_URL#}/admin/staff/pharmacists/add/" class="button blue" style="float:right">Add Pharmacist</a></div>
					{/if}
					{if $pharmacists}
						<table class='regular'>
							<tr>
								<th>Id</th>
								<th>First Name</th>
								<th>Last Name</th>
								<th>Actions</th>
							</tr>
							{foreach $pharmacists as $pharmacist}
								<tr>	
									<td>{$pharmacist->id}</td>
									<td>{$pharmacist->first_name}</td>
									<td>{$pharmacist->last_name}</td>
									<td>
										<a href="{#BASE_URL#}/pharmacist/{$pharmacist->id}/">View</a>
										{if $request->user->belongsToGroups('admin,pharmacist')}
											|
											<a href="{#BASE_URL#}/admin/staff/pharmacists/{$pharmacist->id}/edit/">Edit</a> |
											<a href="{#BASE_URL#}/admin/staff/pharmacists/{$pharmacist->id}/delete/">Delete</a>
										{/if}
									</td>
								</tr>
							{foreachelse}
								<tr><td colspan="2">No Pharmacist Found</td></tr>
							{/foreach}
						</table>
					{else}
						No Pharmacists Found
					{/if}
				</div>
			</div>
		</div>
	</div>
{/block}
