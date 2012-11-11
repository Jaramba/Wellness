set :stages, %w(production staging)
set :default_stage, "staging"
require 'capistrano/ext/multistage'

set :application, "uhai"
set :deploy_to, "~/webapp_releases/#{application}"
set :shared_children, %w(config lib upload database)

set :local_repository, ".git"
set :scm, :git

set :user, "uhai"
set :python_command, "PYTHONPATH=/home/#{user}/webapps/#{application}/lib/python2.7:$PYTHONPATH python2.7"

namespace (:django) do
  desc <<-DESC
    Run the "python manage.py collectstatic" task
  DESC
  task :static do
    run "mkdir -p #{latest_release}/static_root"
    run "cd #{latest_release} && #{python_command} manage.py collectstatic --noinput" 
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
    run "cd #{latest_release} && #{python_command} manage.py reset core records --noinput"
  end
end