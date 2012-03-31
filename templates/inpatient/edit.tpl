{extends "base.tpl"}

{block "page-title"}Inpatient Management: Admin{/block}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Add Inpatient</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="patient[type]" value="inpatient" />
				    	<div class="clearfix">
							<label >Name:</label>
							<div class="input">
								<input type="text" class="required" style="float: left" name="patient[name]" value="{$patient->name}"/>
							</div>
						</div>
						<div class="clearfix">
							<label >Age:</label>
							<div class="input">
								<input type="number" class="required" style="float: left" name="patient[age]" value="{$patient->age}"/>
							</div>
						</div>
						<div class="clearfix">
							<label >Allergies:</label>
							<div class="input">
								<textarea class="required" style="float: left" name="patient[allergies]">{$patient->allergies}</textarea>
							</div>
						</div>
						<div class="clearfix">
							<label >Gender:</label>
							<div class="input">
								<select name="patient[gender]" class="required" style="float: left">
									<option value="">----</option>
									<option value="M" {if $patient->gender=="M"}selected="selected"{/if}>Male</option>
									<option value="F" {if $patient->gender=="M"}selected="selected"{/if}>Female</option>
								</select>
							</div>
						</div>
						<div class="clearfix">
							<label >Note:</label>
							<div class="input">
								<textarea type="text" name="patient[notes]" class="required" style="float: left">{$patient->notes}</textarea>
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