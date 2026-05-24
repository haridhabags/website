# Image Replacement Script for Haridha Website
# Run this in PowerShell to update product images

param(
    [string]$OldImage,
    [string]$NewImage,
    [string]$Version = (Get-Date -Format "yyyyMMdd")
)

# Update index.html with new image path and cache-busting
$content = Get-Content "index.html" -Raw
$content = $content -replace "$OldImage", "$NewImage?v=$Version"
$content | Set-Content "index.html"

Write-Host "Updated $OldImage to $NewImage with version $Version"

# Optional: Copy new image if it exists
if (Test-Path $NewImage) {
    Write-Host "New image file exists: $NewImage"
} else {
    Write-Host "Warning: New image file not found: $NewImage"
}

# Regenerate products.json from the tote_bags_catlog folder so new images appear in the collection
if (Test-Path "./generate-products.ps1") {
    Write-Host "Regenerating products.json from assets/images/tote_bags_catlog..."
    try {
        & .\generate-products.ps1
    } catch {
        Write-Host "Failed to run generate-products.ps1: $_"
    }
} else {
    Write-Host "generate-products.ps1 not found; skipping regeneration."
}