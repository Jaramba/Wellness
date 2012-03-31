{extends "auth/auth_layout.tpl"}

{block "title"}Registration{/block}

{block "extracss"}{/block}
{block "extrajs"}{/block}

{block "body-id"}id="login"{/block}

{block "body"}
	{if isset($errors)}
	    <div id="errors">
	    	{$errors}
	    </div>
	{else if isset($message)}
        <div id="success">
           <div class="clearfix">{$message}</div>
        </div>
    {/if}
    <div class="row">
        <a href="/" class="center block"><img src="{#BASE_URL#}/static/images/biglogo.png" /></a>
        <div class="col_6 pre_3 padding_top_60">
            <div class="widget clearfix">
                <h2>Login</h2>
                <div class="widget_inside">
				    <form class="form" name="newUser" action="." method="post">
				        <div class="clearfix">
				            <label>Username:</label>
				            <div class="input">
				            	<input type="text" name="username" />
				            </div>
				        </div>
				        <div class="clearfix">
				            <label>Password:</label>
				            <div class="input">
				            	<input type="password" name="password" />
				            </div>
				        </div>
				        <div class="clearfix">
				            <label>Confirm:</label>
				            <div class="input">
				            	<input type="password" name="passwordc" />
				            </div>
				        </div>
				        <div class="clearfix">
				            <label>Email:</label>
				            <div class="input">
				            	<input type="text" name="email" />
				            </div>
				        </div>
				        <div class="clearfix">
				            <input type="submit" value="Register"/>
				        </div>
				    </form>
				</div>
			</div>
		</div>
	</div>
{/block}