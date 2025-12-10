# Conversor de Unidades 🔄

A simple command-line unit converter for converting between meters and kilometers.

## Description

This project provides a Python script that allows users to convert between two common length units:
- **Meters (m)** to **Kilometers (km)**
- **Kilometers (km)** to **Meters (m)**

The converter displays the result in both units for reference.

## Features

- ✅ Convert meters to kilometers
- ✅ Convert kilometers to meters
- ✅ Display conversions in both directions
- ✅ User-friendly command-line interface
- ✅ Input validation for valid options

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/juanuniovi/convert_units.git
cd convert_units
```

2. (Optional) Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

## Usage

Run the script:
```bash
python convierte_unidades.py
```

### Example

```
Conversor de unidades
1. Metros a Kilómetros
2. Kilómetros a Metros
Elige opción (1/2): 1
Introduce metros: 5000
5000.0 metros son 5.0 km
5.0 km son 5000.0 metros
```

## How it works

The script provides two conversion functions:

- `metros_a_km(m)`: Converts meters to kilometers (divides by 1000)
- `km_a_metros(km)`: Converts kilometers to meters (multiplies by 1000)

When you run the script:
1. Choose an option (1 or 2)
2. Enter the value you want to convert
3. The script displays the conversion in both units

## Project Structure

```
convert_units/
├── convierte_unidades.py    # Main script
└── README.md                 # This file
```

## Future Improvements

- [ ] Add more unit conversions (miles, feet, etc.)
- [ ] Create a GUI interface
- [ ] Add unit tests
- [ ] Support batch conversions
- [ ] Add configuration file for custom conversion factors

## License

This project is open source and available under the MIT License.

## Author

**juanuniovi** - Initial work

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Create pull requests with improvements

---

Made with ❤️ in 2025
