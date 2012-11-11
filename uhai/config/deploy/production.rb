set :repository, "http://ian:n41l4b@git.synacor.co.ke/#{application}.git"
set :python_command, "PYTHONPATH=/home/#{user}/webapps/#{application}/wellness:$PYTHONPATH python2.7"

set :use_sudo, true
server "uhai-app.cloudapp.net", :app, :web, :primary => true

namespace (:deploy) do
  task :restart do
    run "service gunicorn restart"
    run "kill `ps aux | grep 'run_gunicorn' | grep -v grep | awk '{print $2}'`"
    run "cd #{latest_release} && #{python_command} manage.py collectstatic --noinput"
  end

  task :finalize_update, :except => { :no_release => true } do
    django.static
    django.syncdb
  end
end
