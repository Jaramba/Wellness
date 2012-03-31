{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Nurse Details: {$doctor->first_name} {$doctor->last_name}</h2>
				<div class="widget_inside drugs-search">
					<div class="form">
						<div class="clearfix">
							First Name: {$doctor->first_name}
						</div>
						<div class="clearfix">
							Last Name: {$doctor->last_name}
						</div>
						<div class="clearfix">
							Speciality: {$doctor->speciality}
						</div>
						<div class="clearfix">
							Notes: {$doctor->notes}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/block}