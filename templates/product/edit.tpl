{extends "base.tpl"}

{block "page-title"}Product Management: Admin{/block}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Add Product</h2>
				<div class="widget_inside drugs-search">
					<form class="form" method="POST" action=".">
						<input type="hidden" name="product[type]" value="product" />
				    	<div class="clearfix">
							<label >Name:</label>
							<div class="input">
								<input type="text" class="required" name="product[name]" value="{$product->name}" style="float: left"/>
							</div>
						</div>
						<div class="clearfix">
							<label >Price:</label>
							<div class="input">
								<input type="number" class="required" name="product[price]" value="{$product->price}" style="float: left"/>
							</div>
						</div>
						<div class="clearfix">
							<label >Description:</label>
							<div class="input">
								<textarea type="text" name="product[description]" class="required" style="float: left">{$product->description}</textarea>
							</div>
						</div>
						<div class="clearfix">
							<label for="id_category">Category:</label>
							<div class="input">
								<select name="product[category]" class="required" style="float: left">
									<option>----</option>
									{foreach $categories as $category}
										<option value="{$category->id}" {if isset($product->category->id)}{if $category->id eq $product->category->id } selected="selected" {/if}{/if}>
											{$category->name}
										</option>
									{/foreach}
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