Clear-Host
function read-rss ($URI) {
    [string[]]$codex = @((Invoke-WebRequest -Uri $URI).Content -split "`n")
    [string[]]$linkslst = @(Get-Content 'codex.lst')
    [string]$link = ''
    foreach ($link in $codex) {
        if ($link -imatch '<link>http.*\.si/download/.*\.torrent</link>') {
            [string]$islink = $link -replace ('\s+<link>') -replace ('<\/link>')
            if ($linkslst -notcontains $islink) {
                $islink | Tee-Object -Append 'links.lst'
            }
            else {
                "links.lst contains $islink..."
            }
        }
    }
}
function read-date {
    [datetime]$curr = (Get-Date)
    [datetime]$prev = (Get-Content '.calc\prev.lst')
    [datetime]$next = ($prev.adddays(7))

    if ($curr -ge $next) {
        $curr.ToString() > '.calc\prev.lst'
        return 'run'
    }
    else {
        return 'nothingtoseehere'
    }
}
function read-modtime {
    [datetime]$curr = (Get-Item 'feeds.lst').LastWriteTime
    [datetime]$prev = (Get-Content '.calc\mod.lst')

    if ($curr -gt $prev) {
        $curr.ToString() > '.calc\mod.lst'
        return 'force'
    }
    else {
        return 'nothingtoseehere'
    }
}

if ((read-date) -eq 'run' -OR (read-modtime) -eq 'force' ) {

    $null > 'links.lst'

    [string[]]$feeds = @(Get-Content 'feeds.lst')
    [string]$rss = ''
    foreach ($rss in $feeds) {
        if ($rss -match '^http.*') {
            read-rss $rss
        }
    }

    [string[]]$temp = @(Get-Content 'links.lst')
    [string]$torrent = ''
    foreach ($torrent in $temp) {
        [string]$filename = $torrent -replace ('^http.*\/')
        if (!(Test-Path torrents\$filename)) {
            Start-BitsTransfer $torrent $filename
        }
    }

    if ($temp -match 'http.*') {
        Clear-Host
        '----------------------'
        $temp | Tee-Object -Append 'codex.lst'
        '----------------------'
    
    }
    else {
        Clear-Host
        'THERE ARE NO NEW ITEMS IN THE PROVIDED FEEDS...'
    }

    [string[]]$files = @(Get-ChildItem -File -Filter '*.torrent')
    [string]$file = ''
    foreach ($file in $files) {
        Move-Item $file downloads\torrents\ -Force
    }
}
else {
    Write-Host 'Already run this week. try again on Monday.'
}
