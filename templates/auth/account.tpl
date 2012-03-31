{extends 'auth/auth_layout.tpl'}
{block 'title'}Authentication{/block}

{block "main"}
	<h1>Your Account</h1>
	<p>Welcome to your account page <strong>{$request->user->username}</strong></p>
    {if isset($group->Name)}
    <p>I am a 
    	<strong>
    		{$group->Name}
    	</strong>
    </p>
    {/if}
    <p>You joined on {$signup_date} </p>
{/block}
  

