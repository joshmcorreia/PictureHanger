# PictureHanger

This program helps calculate where to hang pictures on my walls.

All measurements are assumed to be in meters. This tool is created specifically for laser measures because you can get precise measurements.

---

# Choosing Your Design:

## Design 1 - Obstructions (Windows/Doors)
```
     window          door

|    ______         |____|  |
|    |    |         |    |  |
|    |    |         |    |  |
|    ------         |   o|  |
|                   |    |  |
            < ---- >
 X ------- X
```
If you want to center your paintings between the two arrows `< ---- >`, measure the distance from the left wall to the right edge of the window. This area is denoted by `X ------- X`.

`wall_width`: distance of `< ---- >`

`wall_offset`: distance of `X ------- X`

## Design 2 - No Obstructions

```
|                   |
|                   |
|                   |
|                   |
|                   |
 < --------------- >
```
OR
```
                     door

|                   |____|  |
|                   |    |  |
|                   |    |  |
|                   |   o|  |
|                   |    |  |
 < --------------- >
```
If you don't have to worry about an obstruction between the area you are trying to center and a perpendicular wall then these are the settings you want to use.

`wall_width`: distance of `< --------------- >`

`wall_offset`: 0

---

# Configuration Options

### `num_pictures`
```
|                |
|   XXXX  XXXX   |
|   XXXX  XXXX   |
|   XXXX  XXXX   |
|                |
```
Each XXXX block denotes a single painting, so there are `2` paintings in this diagram.

Example config setting:
```
num_pictures: 2
```

### `frame_width`
```
|   <-->         |
|   XXXX  XXXX   |
|   XXXX  XXXX   |
|   XXXX  XXXX   |
|                |
```
The width of each frame.

### `height_from_nail_to_top_of_picture`
This is the height from the nail to the top of the picture.

### `desired_top_of_picture_height`
```
|                 |
|   XXXX  XXXX ^  |
|   XXXX  XXXX |  |
|   XXXX  XXXX |  |
|              v  |
```
This is the desired height of the top of the picture

### `distance_between_frames`
```
|       <--->      |
|   XXXX     XXXX  |
|   XXXX     XXXX  |
|   XXXX     XXXX  |
|                  |
```
OR
```
|       <--->    <--->      |
|   XXXX     XXXX     XXXX  |
|   XXXX     XXXX     XXXX  |
|   XXXX     XXXX     XXXX  |
|                           |
```
This is the distance between each frame.

---

# Execution:
After setting the values in the config file, run:
```
cargo run
```
