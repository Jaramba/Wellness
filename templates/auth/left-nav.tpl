{if !$request->user->isUserLoggedIn()}
	<ul>
	    <li><a href="{#BASE_URL#}/">Home</a></li>
	    <li><a href="{#BASE_URL#}/auth/login/">Login</a></li>
	    <li><a href="{#BASE_URL#}/contacts/">Contacts</a></li>
	</ul>
{else}
	<ul>
		<li><a href="{#BASE_URL#}/">Home</a></li>
		<li><a href="{#BASE_URL#}/auth/logout/">Logout</a></li>
		<li><a href="{#BASE_URL#}/auth/account/">Account Home</a></li>
		<li><a href="{#BASE_URL#}/auth/change-password/">Change password</a></li>
	    <li><a href="{#BASE_URL#}/auth/update-email-address/">Update email address</a></li>
	</ul>
{/if}