
set :application, "wellington"
set :deploy_to, "~/webapp_releases/wellington"
set :shared_children, %w(config lib upload database)

set :repository, "~/hg/repos/wellington"
set :scm, :mercurial

set :user, "synacor"
set :use_sudo, false
set :python_command, "PYTHONPATH=/home/synacor/webapps/wellington/lib/python2.7:$PYTHONPATH python2.7"

server "synacor.co.ke", :app, :web, :primary => true

namespace :deploy do

  task :restart do
    run "/home/synacor/webapps/wellington/apache2/bin/restart"
  end

  task :finalize_update, :except => { :no_release => true } do

    django.static
    django.syncdb

  end

end

namespace (:django) do

  desc <<-DESC
    Run the "python manage.py collectstatic" task
  DESC
  task :static do
    run "mkdir -p #{latest_release}/static"
    run "cd #{latest_release} && #{python_command} manage.py collectstatic --noinput" 
  end

  desc <<-DESC
    Run the "python manage.py index --rebuild" task
  DESC
  task :search do
    run "cd #{latest_release} && #{python_command}  manage.py index --rebuild"
  end

  desc <<-DESC
    Run the "python manage.py syncdb" task
  DESC
  task :syncdb do
    run "cd #{latest_release} && #{python_command} manage.py syncdb --noinput"
  end

  desc <<-DESC
    Run the "python manage.py reset web" task
  DESC
  task :reset do
    run "cd #{latest_release} && #{python_command} manage.py reset web --noinput"
  end

end
