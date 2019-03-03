#Email address declaration

$to = "chinmaykumar.nayak@libertymutual.com"
$from = "PersonalCare@Automation.com"
$smtp_server = "smtprelay.lmig.com"


#Time Feed


#$startTime = 25200
$interval = 3600
$counter = 0
<#

#$startTime = 12
$interval = 4
$counter = 0
#>

For($startTime = 28800;$startTime -ne 0){
    Function alertEmail {
        Send-MailMessage -From $from -To $to -smtpServer $smtp_server -Subject "Reminder From Docker" -Body "Drink Water.Its an hour now.`nTimeleft=$startTime seconds`n`nThank You `n`n`nDo Not Reply to this Email"
    }
    
    #Will loop for 60 mins(3600 secs)
    while ($counter -ne $interval){
        Start-Sleep 1
        $counter += 1
    }
    
    alertEmail
    $startTime = $startTime - $counter
    $counter = 0
}

