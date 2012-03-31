{extends "base.tpl"}

{block "container"}
	<div class="row clearfix">
		<div class="col_12">
			<div class="widget clearfix" style="min-height: 300px;">
				<h2>User Detail</h2>
				<div class="widget_inside drugs-search">
					<div class="form">
						<div class="clearfix">
							Id: {$user->id}
						</div>
						<div class="clearfix">
							Username: {$user->name}
						</div>
						<div class="clearfix">
							Email: {$user->email}
						</div>
						<div class="clearfix">
							{if $request->user->id eq $user->id}
								<a class="button blue" href="{#BASE_URL#}/auth/change-password/">Change Password</a>
							{/if}
							<a class="button" href="{#BASE_URL#}/admin/users/{$user->id}/edit/">Edit</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/block}
