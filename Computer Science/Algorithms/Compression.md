### Dictionary Encoding
Used on text files


### Run-Length Encoding
Used on binary files (image, audio)
- Takes small portions of the data, and recreate it in a smaller form for transmission
- Eliminates repeated values / patterns
#### Example:
- `"aaaa" -> "a"x4`  
- `"ababac" -> "ab"x2 "ac"x1`