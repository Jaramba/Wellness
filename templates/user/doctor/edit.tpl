{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>{if $doctor->id}Edit{else}Add{/if} Doctor</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="staff[id]" value="{$doctor->id}" />
						<input type="hidden" name="staff[type]" value="doctor" />
						<div class="clearfix">
							<label for="id_first_name">First Name:</label>
							<div class="input">
								<input type="text" class="required" name="staff[first_name]" value="{$doctor->first_name}" style="float: left" />
							</div>
						</div>
						<div class="clearfix">
							<label for="id_last_name">Last Name:</label>
							<div class="input">
								<input type="text" class="required" name="staff[last_name]" value="{$doctor->last_name}" style="float: left"/>
							</div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">Speciality:</label>
							<div class="input">
								<input type="text" class="required" name="staff[speciality]" value="{$doctor->speciality}" style="float: left"/>
							</div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">Notes:</label>
							<div class="input">
								<textarea name="staff[notes]">{$doctor->notes}</textarea>
							</div>
						</div>
						<div class="clearfix">
							<label for="id_speciality">User:</label>
							<div class="input">
								<select name="user" class="required" style="float: left">
									<option value='null'>----</option>
									{foreach $users as $user}
										<option value='{$user->id}' {if isset($parent_user)}{if $user->id eq $parent_user->id}selected="selected"{/if}{/if}>
											{$user->username}
										</option>
									{/foreach}
								</select>
							</div>
						</div>
						<div class="clearfix">
							<div class="input grey-highlight">
								<input type="submit" class="button blue" value="Edit">
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
{/block}