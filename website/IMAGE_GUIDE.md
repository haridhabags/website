# Haridha Image Management Guide

## Current Images in Use:
- 11.png (4.59MB) - Everyday Cotton Tote
- 12.png (4.73MB) - Market Carryall
- 13.png (4.70MB) - Work Tote
- 14.png (4.76MB) - Compact City Tote
- 15.png (5.31MB) - Travel Weekender
- tote-1.jpg (0.06MB) - Minimalist Tote

## Available Replacement Images:
- 5.png, 7.png, 8.png, 9.png, 16.png, 17.png, 18.png, 19.png, 45.png

## To Replace an Image:
1. Copy new image to: assets/images/tote_bags_catlog/
2. Update the src path in index.html
3. Add cache-busting parameter: ?v=NEWVERSION

Example:
```html
<!-- Old -->
<img src="assets/images/tote_bags_catlog/11.png" alt="...">

<!-- New -->
<img src="assets/images/tote_bags_catlog/5.png?v=20240415" alt="...">
```