{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Inpatient Drug Assign</h2>
				<div class="widget_inside drugs-search">
					<form action="." method="POST" class="form">
						<div class="clearfix">
							<label>Name:</label>
							<div class="input"> 
								{$inpatient->name}
							</div>
						</div>
						<div class="clearfix">
							<label >Product:</label>
							<div class="input">
								<select name="product">
									<option value="">----</option>
									{foreach $products as $product}
										<option value="{$product->id}">{$product->name}</option>
									{/foreach}
								</select>
							</div>
						</div>
						<div class="clearfix">
							<label>Quantity:</label>
							<div class="input"> 
								<input type="text class="required" name="quantity"/>
							</div>
						</div>
						{if $request->user->belongsToGroups('nurses')}
							<div class="clearfix">
								<input type="submit" class="button blue" value="Approve"/>
							</div>
						{/if}
					</form>
				</div>
			</div>
		</div>
	</div>
{/block}
