Get-ComputerInfo | Select-Object WindowsRegisteredOwner, WindowsProductName, CsName, CsNetworkAdapters, CsPrimaryOwnerName, CsUserName, OsSerialNumber | Out-File -FilePath "pcinfo.txt"
"------- INFORMACAO DOS IP --------" | Out-File -FilePath "pcinfo.txt"-Append
Get-NetIPAddress -AddressFamily IPv4 | Select-Object IPAddress, InterfaceAlias | Format-Table | Out-File -FilePath "pcinfo.txt" -Append