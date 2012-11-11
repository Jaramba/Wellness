set :repository, "~/webapps/git/repos/uhai.git"
set :python_command, "PYTHONPATH=/home/uhai/webapps/uhai/lib/python2.7:$PYTHONPATH python2.7"

set :use_sudo, false
server "synacor.co.ke", :app, :web, :primary => true

namespace (:deploy) do
  task :restart do
    run "~/webapps/uhai/apache2/bin/restart"
  end

  task :finalize_update, :except => { :no_release => true } do
    django.static
    django.syncdb
  end
end
