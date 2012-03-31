{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>{if $nurse->id}Edit{else}Add{/if} Nurse</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="order[type]" value="order" />
						<div class="clearfix">
							<label for="id_first_name">First Name:</label>
							<div class="input">
								<input type="text" name="order[first_name]" value="" />
							</div>
						</div>
						<div class="clearfix">
							<label for="id_last_name">Last Name:</label>
							<div class="input">
								<input type="text" name="order[last_name]" value="" />
							</div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">Speciality:</label>
							<div class="input">
								<input type="text" name="order[speciality]" value="" />
							</div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">Notes:</label>
							<div class="input">
								<textarea name="order[notes]"></textarea>
							</div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">User:</label>
							<div class="input">
								<select name="user">
									<option value='null'>----</option>
									{html_options options=$users selected=$nurse->ownUser[0]->id}
								</select>
							</div>
						</div>
						<div class="clearfix grey-highlight">
							<div class="input no-label">
					        	<input type="submit" class="button blue" value="Save">
					        </div>
					    </div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/block}