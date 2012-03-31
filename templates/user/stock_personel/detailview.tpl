{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Nurse Details: {$stock_personel->first_name} {$stock_personel->last_name}</h2>
				<div class="widget_inside drugs-search">
					<div class="form">
						<div class="clearfix">
							First Name: {$stock_personel->first_name}
						</div>
						<div class="clearfix">
							Last Name: {$stock_personel->last_name}
						</div>
						<div class="clearfix">
							Speciality: {$stock_personel->speciality}
						</div>
						<div class="clearfix">
							Notes: {$stock_personel->notes}
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/block}