param([int]$Port = 8000)

$Listener = New-Object System.Net.HttpListener
$Listener.Prefixes.Add("http://localhost:$Port/")
$Listener.Start()
Write-Host "Server at http://localhost:$Port | Press Ctrl+C to stop"

while ($Listener.IsListening) {
    $Context = $Listener.GetContext()
    $Request = $Context.Request
    $Response = $Context.Response
    $LocalPath = $Request.Url.LocalPath
    if ($LocalPath -eq "/") { $LocalPath = "/index.html" }
    $FilePath = Join-Path (Get-Location) ($LocalPath.TrimStart('/').Replace('/', '\'))
    
    if (Test-Path $FilePath -PathType Leaf) {
        $Content = [System.IO.File]::ReadAllBytes($FilePath)
        $ext = [System.IO.Path]::GetExtension($FilePath).ToLower()
        $mimes = @{".html"="text/html;charset=utf-8"; ".css"="text/css"; ".js"="application/javascript"; ".json"="application/json"; ".png"="image/png"; ".jpg"="image/jpeg"; ".gif"="image/gif"; ".webp"="image/webp"; ".mp4"="video/mp4"}
        $Response.ContentType = $mimes[$ext] -or "application/octet-stream"
        $Response.ContentLength64 = $Content.Length
        $Response.OutputStream.Write($Content, 0, $Content.Length)
        Write-Host "[OK] $LocalPath"
    } else {
        $Response.StatusCode = 404
        $buf = [System.Text.Encoding]::UTF8.GetBytes("404")
        $Response.ContentLength64 = $buf.Length
        $Response.OutputStream.Write($buf, 0, $buf.Length)
        Write-Host "[ERR] $LocalPath"
    }
    $Response.Close()
}
