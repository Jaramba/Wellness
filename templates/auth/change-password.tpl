{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>Change Password</h2>
				<div class="widget_inside drugs-search">
			    {if isset($errors)}
			        <div id="errors">{$errors}</div>
			    {/if}
			    {if isset($success_message)}
			    	<div id="success"><div class="clearfix">{$success_message}</div></div>
			    {/if}
		        <form class="form" name="changePass" action="." method="post">
		            <div class="clearfix">
		                <label>Password:</label>
		                <div class="input"><input type="password" name="password" /></div>
		            </div>
		            <div class="clearfix">
		                <label>New Pass:</label>
		                <div class="input"><input type="password" name="passwordc" /></div>
		            </div>
		            <div class="clearfix">
		                <label>Confirm Pass:</label>
		                <div class="input"><input type="password" name="passwordcheck" /></div>
		            </div>
		    		<div class="clearfix grey-highlight">
						<div class="input no-label">
				        	<input type="submit" class="button blue" value="Change">
				        </div>
				    </div>
		        </form>
			</div>
		</div>
	</div>
{/block}