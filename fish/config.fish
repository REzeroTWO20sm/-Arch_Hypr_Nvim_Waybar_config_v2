   if status is-interactive
       # Commands to run in interactive sessions
       if test -f /home/zero/system_configs/fish-greeting.txt
           cat /home/zero/system_configs/fish-greeting.txt
       end
   end

   # Clear the default greeting
   set -g fish_greeting ""

   # Add any other configuration lines below
   set -g PATH /home/zero/miniconda3/bin $PATH
   set -g PATH /home/zero/tools/node-v14.15.4-linux-x64/bin $PATH
   set -x QT_QPA_PLATFORMTHEME "qt5ct"
