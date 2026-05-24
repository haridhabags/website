# generate-products.ps1 - create products.json from images
<#
Scans assets/images/tote_bags_catlog and writes a simple products.json
Run: .\generate-products.ps1
#>

Param(
    [string]$ImageFolder = "assets/images/tote_bags_catlog",
    [string]$OutputFile = "products.json",
    [int]$DefaultPrice = 699
)

if (-not (Test-Path $ImageFolder)) {
    Write-Error "Image folder not found: $ImageFolder"
    exit 1
}

$images = Get-ChildItem -Path $ImageFolder -File | Where-Object { $_.Extension -match '\.(png|jpg|jpeg|webp)$' } | Sort-Object Name
$products = @()
foreach ($img in $images) {
    $name = [System.IO.Path]::GetFileNameWithoutExtension($img.Name)
    # Make a friendly title: replace -,_, and numbers with spaces
    $title = $name -replace '[-_0-9]+' , ' '
    # Use CultureInfo for proper title case
    $title = (Get-Culture).TextInfo.ToTitleCase($title.ToLower()).Trim()
    $obj = [PSCustomObject]@{
        name = $title
        price = $DefaultPrice
        tags = @()
        img = "$ImageFolder/$($img.Name)"
        badge = ""
        alt = "Haridha Tote - $title"
    }
    $products += $obj
}

$products | ConvertTo-Json -Depth 4 | Set-Content -Path $OutputFile -Encoding UTF8
Write-Host "Wrote $($products.Count) products to $OutputFile"