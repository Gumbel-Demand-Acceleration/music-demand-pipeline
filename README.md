## Current Status

This project currently converts canonical song-country-week demand data into fixed-length weekly demand vectors.

Current pipeline:

- Load raw demand data
- Validate canonical schema
- Build 26-week demand vectors
- Save model-ready parquet output

Next milestone:

- Add Soundcharts loader once provider data is available
- Add B-spline label generation compatible with the existing sound-wave model