# Create thumbnails with ImageMagick

## The simplest way

You have a folder (`pictures`) containing a lot of big jpg files.

Just create a `thumbs` subfolder, and open a terminal in `pictures`.

Install ImageMagick and type this:
```
# mogrify -format jpeg -path thumbs -thumbnail 1024x1024 *.jpg
```

You'll find the thumbnails inside the `pictures/thumbs`.
