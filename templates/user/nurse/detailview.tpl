{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Nurse Details: {$nurse->first_name} {$nurse->last_name}</h2>
				<div class="widget_inside drugs-search">
					<div class="form">
						<div class="clearfix">
							First Name: {$nurse->first_name}
						</div>
						<div class="clearfix">
							Last Name: {$nurse->last_name}
						</div>
						<div class="clearfix">
							Speciality: {$nurse->speciality}
						</div>
						<div class="clearfix">
							Notes: {$nurse->notes}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/block}