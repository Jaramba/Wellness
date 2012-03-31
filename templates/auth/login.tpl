{extends 'base.tpl'}
{block 'title'}Authentication{/block}

{block "extracss"}{/block}
{block "extrajs"}{/block}

{block "body-id"}id="login"{/block}

{block "body"}
	{if isset($errors)} <div id="errors">{$errors}</div>{/if}
	<div class="container">
	    <div class="row">
	        <a href="/" class="center block"><img src="{#BASE_URL#}/static/images/biglogo.png" /></a>
	        <div class="col_6 pre_3 padding_top_60">
	            <div class="widget clearfix">
	                <h2>Login</h2>
	                <div class="widget_inside">
	                    <div class="form">
	                    	<form method="POST" action=".">
		                        <div class="clearfix">
		                            <label>Username</label>
		                            <div class="input">
		                                <input id="username" type="text" class="validate[required]" name="username" class="xlarge"/>
		                            </div>
		                        </div>
		                        <div class="clearfix">
		                            <label>Password</label>
		                            <div class="input">
		                                <input id="password" type="password" class="validate[required]" name="password" class="xlarge"/>
		                            </div>
		                        </div>
		                        <div class="clearfix">
		                            <div class="input no-label">
		                                <input type="checkbox" /> Remember me?
		                            </div>
		                        </div>
		                        <div class="clearfix grey-highlight">
		                            <div class="input no-label ">
		                                <input type="submit" class="button blue" value="Login"/>
		                                <input type="reset" class="button" value="Reset"/>
		                            </div>
		                        </div>
		                    </form>
	                    </div>
	                </div>
	            </div>
	        </div>
	    </div>
	</div>
{/block}
