<# Martin Gabriel Mejia Hurtado #>
$dir = (get-command powershell.exe).Path
$trigger = New-ScheduledTaskTrigger -Daily -At "06:00pm"
$action = New-ScheduledTaskAction -Execute $dir -Argument "send_sysinfo.ps1" -workingDirectory "<direccion>"
Register-ScheduledTask send_sysinfo -Trigger $trigger -Action $action -Description "Tarea que ejecuta send_sysinfo"
