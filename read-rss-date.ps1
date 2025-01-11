[datetime]$curr = (Get-Date)
[datetime]$prev = (Get-Content '.calc\prev.lst')
[datetime]$next = ($prev.adddays(7))

if ($curr -ge $next) {
    'bob'
    #$curr.ToString() > '.calc\prev.lst'
}


[datetime]$curr = (Get-Item 'feeds.lst').LastWriteTime
[datetime]$prev = (Get-Content '.calc\mod.lst')

if ($curr -gt $prev) {
    $curr.ToString() > '.calc\mod.lst'
}
