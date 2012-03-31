{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Nurse Details: {$pharmacist->first_name} {$pharmacist->last_name}</h2>
				<div class="widget_inside drugs-search">
					<div class="form">
						<div class="clearfix">
							First Name: {$pharmacist->first_name}
						</div>
						<div class="clearfix">
							Last Name: {$pharmacist->last_name}
						</div>
						<div class="clearfix">
							Speciality: {$pharmacist->speciality}
						</div>
						<div class="clearfix">
							Notes: {$pharmacist->notes}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/block}