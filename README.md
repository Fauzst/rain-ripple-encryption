# Rain Ripple Encryption
The Rain Ripple–Based Algorithm is a chaos-driven key generation system designed for secure file encryption.
It leverages the natural randomness of rain ripple patterns, combining computer vision and chaotic dynamics to produce unpredictable encryption keys.

First, the algorithm uses a YOLOv8 model to detect and track rain ripples from real-world footage.
The model extracts parameters such as position, height, width, and count of each identified ripple.
These parameters are then fed into the Lorenz system, a well-known chaotic mathematical model, to amplify and transform the captured data into a complex, highly sensitive key sequence.

The generated key is subsequently used for file encryption, ensuring that each encryption process is uniquely influenced by naturally occurring, non-reproducible rain ripple patterns.

## Features
- This system is used to encrypt files using the randomness of rain ripples.
- To increase randomness, it utilizes Lorenz system--- three ordinary differential equation that models atmospheric convection and simulates a chaotic system.
- In a chaotic system, one slight changes in parameter input would greatly affect the output.
