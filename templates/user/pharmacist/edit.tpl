{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>{if $pharmacist->id}Edit{else}Add{/if} Pharmacist</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="staff[id]" value="{$pharmacist->id}" />
						<input type="hidden" name="staff[type]" value="pharmacist" />
						<div class="clearfix">
							<label for="id_first_name">First Name:</label>
							<div class="input"><input type="text" class="required" name="staff[first_name]" value="{$pharmacist->first_name}" style="float: left"/></div>
						</div>
						<div class="clearfix">
							<label for="id_last_name">Last Name:</label>
							<div class="input"><input type="text" class="required" name="staff[last_name]" value="{$pharmacist->last_name}" style="float: left"/></div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">Speciality:</label>
							<div class="input"><input type="text" class="required" name="staff[speciality]" value="{$pharmacist->speciality}" style="float: left"/></div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">Notes:</label>
							<div class="input">
								<textarea name="staff[notes]">{$pharmacist->notes}</textarea>
							</div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">User:</label>
							<div class="input">
								<select name="user" style="float: left">
									<option value='null'>----</option>
									{html_options options=$users selected=$pharmacist->ownUser[0]->id}
								</select>
							</div>
						</div>
						<div class="clearfix">
							<div class="input grey-highlight">
								<input type="submit" class="button blue" value="Save">
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/block}