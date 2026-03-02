# Squish Pad
A fully 3D-printable, true gasket-mounted 4x4 macropad engineered for a premium, ultra-smooth typing experience.

# Features
	16-Key Matrix + Rotary Encoder
	Engineered Leaf-Spring Plate providing a bouncy, trampoline-like typing fee
	Utilizes 3D-printed "slip-on" gasket socks to sandwich the plate tabs, completely isolating the plate and PCB from the outer case.
	Acoustic PCB Cushion

# Rendering
<img width="1248" height="832" alt="image" src="https://github.com/user-attachments/assets/728e8d61-afb4-4477-9a57-c6ee6c1557d6" />

# Schematic
<img width="748" height="518" alt="hackpad schematic" src="https://github.com/user-attachments/assets/d95da132-57f5-4336-a94b-71dcf3066550" />

# PCB
<img width="389" height="390" alt="hackpad pcb" src="https://github.com/user-attachments/assets/d765ff5e-0c80-4e9e-b974-6ec1cd21c03e" />

# BOM
	1x unsoldered Seeed XIAO RP2040
	16x through-hole 1N4148 Diodes
	15x MX-Style switches
	1x EC11 Rotary encoders
	15x white blank DSA keycaps
	16x SK6812 MINI-E LEDs
	4x M3x16mm screws
	4x M3x5mx4mm heatset inserts
	1x Printed PCB
	1x Case (All parts, guide below)

# Printing Guide

> **If you dont have TPU:** Print the gaskets with PLA/PETG and don't print the cushion. The macropad will still be slightly flexible


| Part | Material | Key Settings |
| :--- | :--- | :--- |
| **Top & Bottom Case** | PLA-CF / PLA | Wall Loops: **5** \| Infill: **25% Gyroid** \| Layer: **0.16mm** |
| **Leaf-Spring Plate** | PETG | Wall Loops: **4** \| Layer: **0.15mm** \| Top/Bottom Layers: **5** |
| **Gaskets (x4)** | 95A TPU | Walls: **2** \| Top/Bottom: **0** \| Infill: **12% Gyroid** \| Speed: **3.5mm³/s** |
| **Cushion** | 95A TPU | Walls: **1** \| Top/Bottom: **0** \| Infill: **6% Gyroid** \| Speed: **3.5mm³/s** |

> **Note:** For the TPU parts, setting Top and Bottom layers to **0** is critical, this exposes the Gyroid infill to create the "squish" effect.
