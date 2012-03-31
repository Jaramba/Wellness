{extends "base.tpl"}	

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Inpatients</h2>
				<div class="widget_inside drugs-search">
					{if $request->user->belongsToGroups('admin')}
						<div id="add" style="width:100%;clear:both"><a href="{#BASE_URL#}/patients/inpatients/add/" class="button blue" style="float:right">Add Inpatient</a></div>
					{/if}
					{if $patients}
						<table class='regular'>
							<tr>
								<th>Id</th>
								<th>Name</th>
								<th>Age</th>
								<th>Gender</th>
								<th>Actions</th>
							</tr>
							{foreach $patients as $inpatient}
								<tr>	
									<td>{$inpatient->id}</td>
									<td><a href="{#BASE_URL#}/patients/inpatients/{$inpatient->id}/">{$inpatient->name}</a></td>
									<td>{$inpatient->age}</td>
									<td>{$inpatient->gender}</td>
									<td>
										{if $request->user->belongsToGroups('admin')}
											<a href="{#BASE_URL#}/patients/inpatients/{$inpatient->id}/edit/">Edit</a> |
											<a href="{#BASE_URL#}/patients/inpatients/{$inpatient->id}/delete/">Delete</a>
										{/if}
										{if $request->user->belongsToGroups('nurses')}
											| <a href="{#BASE_URL#}/patients/inpatients/{$patient->id}/assign-drug/">Assign Drug</a>
										{/if}
									</td>
								</tr>
							{foreachelse}
								<tr><td colspan="2">No Inpatients Found</td></tr>
							{/foreach}
						</table>
					{else}
						No Inpatients Found
					{/if}
				</div>
			</div>
		</div>
	</div>
{/block}