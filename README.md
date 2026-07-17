<div align="center">
<a id="top"></a>
<img src="resources/QTVdocs.png" alt="Q-TV" width="340">
<h3>Your apps. Your screen. Your way.</h3>

A modern TV interface for your PC. Q-TV brings a simple, remote-friendly<br>
experience to your desktop with an app-first design.

<p>
<img src="https://img.shields.io/badge/Status-Early%20Development-purple?style=flat-square">
<img src="https://img.shields.io/badge/Python 3.x-3776AB?logo=python&logoColor=white&style=flat-square">
<img src="https://img.shields.io/badge/PySide6-41CD52?logo=qt&logoColor=white&style=flat-square">
<img src="https://img.shields.io/badge/Powered by-Fedora%20Minimal-51A2DA?logo=fedora&logoColor=white&style=flat-square">
<img src="https://img.shields.io/badge/Waydroid-00A884?logo=android&logoColor=white&style=flat-square">
<br>
<img src="https://img.shields.io/github/license/nbao210/qtv-shell?style=flat-square&cacheSeconds=60">
<img src="https://img.shields.io/github/stars/nbao210/qtv-shell?style=flat-square&logo=github&cacheSeconds=60">
<img src="https://img.shields.io/github/forks/nbao210/qtv-shell?style=flat-square&logo=github&cacheSeconds=60">
<img src="https://img.shields.io/github/issues/nbao210/qtv-shell?style=flat-square&logo=github&cacheSeconds=60">
</p> 

#### Designed for

[![Fedora](https://img.shields.io/badge/Fedora-294172?style=flat-square&logo=fedora&logoColor=white)](https://fedoraproject.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![openSUSE](https://img.shields.io/badge/openSUSE-73BA25?style=flat-square&logo=opensuse&logoColor=white)](https://www.opensuse.org/)
[![Arch Linux](https://img.shields.io/badge/Arch_Linux-1793D1?style=flat-square&logo=archlinux&logoColor=white)](https://archlinux.org/)
[![Pop! OS](https://img.shields.io/badge/Pop!_OS-59C7B6?style=flat-square&logo=popos&logoColor=white)](https://pop.system76.com/)
[![Linux Mint](https://img.shields.io/badge/Linux_Mint-87CF3E?style=flat-square&logo=linuxmint&logoColor=white)](https://linuxmint.com/)
[![Zorin OS](https://img.shields.io/badge/Zorin%20OS-0085FF?style=flat-square&logo=zorin&logoColor=white)](https://zorin.com/)
[![Debian](https://img.shields.io/badge/Debian-A81D33?style=flat-square&logo=debian&logoColor=white)](https://www.debian.org/)
[![RHEL](https://img.shields.io/badge/RHEL-EE0000?style=flat-square&logo=redhat&logoColor=white)](https://www.redhat.com/)
[![NixOS](https://img.shields.io/badge/NixOS-5277C3?style=flat-square&logo=nixos&logoColor=white)](https://nixos.org/)
[![AppImage](https://img.shields.io/badge/AppImage-Supported-6F42C1?style=flat-square&logo=appimage&logoColor=white)](https://appimage.org/)

[Englist](README.md) | [Tiếng Việt](README-vi.md)

</div>

## Screenshots

<div align="center">
<img src="resources/docs/screenshot.png" alt="screenshot" width="720">
<br>
<sub>Q-TV Shell interface · App launcher and TV-style navigation</sub>

</div>


## Table of Contents

- [About](#about)
- [Status](#status)
- [Features](#features)
- [Target Platforms](#target-platforms)
- [Requirements And Recommendations](#requirements-and-recommendations)
- [Installation](#installation)
- [Roadmap](#roadmap)
- [Languages](#languages)
- [Contributing](#contributing)
- [FAQ](#faq)
- [License](#license)

## About

Q-TV is an open-source Smart TV platform designed to transform PCs and laptops into a TV-like experience while giving older hardware a new purpose.

Inspired by modern Smart TV systems, Q-TV provides a remote-friendly interface built on Linux. Instead of relying on Android TV x86, Q-TV uses Linux as its foundation, allowing greater customization, hardware flexibility, and future possibilities such as dedicated TV boxes or OEM integrations.

Q-TV combines a TV-focused shell, native applications, and Android TV application support through Waydroid. The project aims to become both a Linux-powered TV operating system and an open TV platform for PCs, with the official image planned to be based on Fedora Minimal.
## Status
<div align="center"><img src="https://img.shields.io/badge/Status-Early%20Development-purple?style=flat-square" width=180></div>

Q-TV is currently in early development and is not intended for daily use yet. The project is focused on building the core TV experience, including the shell, navigation system, and application ecosystem.

| Component | Status |
|---|---|
| Q-TV Shell | 🟡 Beta |
| Navigation System | 🟠 Experimental |
| Wallpaper System | 🟠 Experimental |
| Native Applications | 🔵 Early Development |
| Waydroid Integration | ⚪ Planned |
| Q-TV Image | ⚪ Planned |

> [!NOTE]
> Features may change, break, or be redesigned as the project evolves.
> The project is still in early development, with no official release version yet.

## Features

### TV Experience

- 📺 Smart TV-inspired interface designed for large screens and remote-friendly navigation.
- 🎮 D-pad style navigation with keyboard and remote input support.
- ✨ Smooth focus animations and visual feedback for TV-style interaction.
- 🖼️ Dynamic wallpaper system with support for multiple wallpaper providers.

### Application Platform

- 🚀 Q-TV Shell providing a unified launcher experience.
- 🧩 Native Q-TV applications designed specifically for the TV interface.
- 📱 Android TV application integration through Waydroid.
- 🛒 Q-TV Store for discovering and managing applications.
- 🔌 Extension system for adding new capabilities, such as custom wallpaper providers.

### Built-in Applications

Q-TV includes a growing collection of native applications:

| Application | Description |
|---|---|
| Settings | Manage Q-TV preferences and system configuration |
| File Manager | Browse and manage local files |
| Q-TV Entertainment Center | Watch live TV, movies, and access local media content |
| Store | Discover and manage Q-TV applications |

### Platform Integration

- 🐧 Linux-based architecture designed for flexibility and customization.
- 💻 Support for repurposing older PCs and laptops as Smart TV devices.
- 📦 Planned Q-TV Image with a dedicated TV-focused Linux environment.
- 🔧 Planned first-time setup experience (OOBE) for easier device configuration.


## Target Platforms

Q-TV is primarily designed for Linux environments, with a focus on modern desktop systems using Wayland and Qt support.

The Q-TV Shell is designed to run across different Linux distributions. Currently tested environments include:
<div align="center">
<p>
<a href="https://fedoraproject.org/"><img src="https://img.shields.io/badge/Fedora-Tested-487E02?style=flat-square&logo=fedora&logoColor=white&labelColor=005C94" height="25"></a>
<a href="https://zorin.com/"><img src="https://img.shields.io/badge/Zorin%20OS-Tested-487E02?style=flat-square&logo=zorin&logoColor=white&labelColor=0085FF" height="25"></a>
<a href="https://ubuntu.com/"><img src="https://img.shields.io/badge/Ubuntu-Tested-487E02?style=flat-square&logo=ubuntu&logoColor=white&labelColor=E95420" height="25"></a>
<a href="https://pop.system76.com/"><img src="https://img.shields.io/badge/Pop!_OS-Tested-487E02?style=flat-square&logo=popos&logoColor=white&labelColor=59C7B6" height="25"></a>
<a href="https://linuxmint.com/"><img src="https://img.shields.io/badge/Linux_Mint-Tested-487E02?style=flat-square&logo=linuxmint&logoColor=white&labelColor=87CF3E" height="25"></a>
</p>
</div>

> [!NOTE]
> Other Linux distributions with compatible Wayland and Qt environments are expected to work.
> Compatibility may vary depending on the desktop environment, graphics stack, and system configuration.

### Official Q-TV Image

The official Q-TV Image is planned as a dedicated TV-focused Linux environment based on Fedora Minimal.

| Target Hardware | Status |
|---|---|
| Older PCs and laptops | Planned |
| Mini PCs | Planned |
| ARM devices (e.g. Raspberry Pi) | Future consideration |

### Architecture

| Architecture | Status |
|---|---|
| x86_64 | Primary target |
| ARM64 | Not currently planned |

> [!NOTE]
> Windows support is not currently planned for the official Q-TV project. However, future ports or community-driven implementations may be possible.

## Requirements And Recommendations

Q-TV is designed to run on a wide range of PC hardware, including older systems repurposed as Smart TV devices.

### Minimum Requirements

| Component | Requirement |
|---|---|
| 🧠 CPU | Intel Core i3 4th Gen (Haswell) or newer<br>AMD Ryzen 3 or equivalent |
| 💾 Memory | 6GB RAM |
| 📂 Storage | 8GB available storage |
| 🎮 Graphics | Integrated graphics or entry-level dedicated GPU (e.g. NVIDIA GTX 750 Ti class) |
| 🖥️ Display | 1024×768 or higher |

### Recommended Requirements

| Component | Requirement |
|---|---|
| 🧠 CPU | Intel Core i5 7th Gen or newer<br>AMD Ryzen 5 or equivalent |
| 💾 Memory | 8GB RAM or more |
| 📂 Storage | 8GB SSD or more |
| 🎮 Graphics | Modern integrated graphics or dedicated GPU |
| 🖥️ Display | 1920×1080 recommended, 4K supported |

> [!NOTE]
> Performance may vary depending on the desktop environment, graphics driver, and enabled features.
> Additional requirements may apply when using Android TV applications through Waydroid.

### Additional Recommendations

- ⌨️ A keyboard, [Bluetooth remote](https://www.google.com/search?tbm=shop&q=bluetooth+remote+tv), or IR receiver is recommended for TV-style navigation.
- 🔵 Bluetooth support is required when using Bluetooth-based controllers or remotes. (You can also use a [Bluetooth USB dongle](https://www.google.com/search?tbm=shop&q=bluetooth+usb+dongle)).
- 🌐 A Wi-Fi or network connection is required for online services such as streaming, wallpaper providers, and application downloads.
- 📺 HDMI-CEC support is optional for controlling Q-TV through a TV remote.

> [!IMPORTANT]
> For the best Q-TV experience, use a remote that provides standard input methods. Some OEM TV remotes may not work correctly due to proprietary protocols or missing HID support.

> [!NOTE]
> Keyboard and mouse input are supported for development and setup, but a remote control is recommended for the intended TV experience.

For the best experience with Q-TV, we recommend using remote controls that support standard USB HID (2.4GHz) or Bluetooth HID (including Bluetooth Low Energy - BLE).

The following devices are recommended based on HID compatibility and TV-style usability:

| Device | Type | Notes |
|---|---|---|
| **G20S / G20S Pro / G20S Pro BT** | Air Mouse | Recommended. Supports gyroscope control and provides accurate pointer movement. |
| **MX3** / **Mini KM900** | Air Mouse + Keyboard | Includes a rear QWERTY keyboard for convenient text input. |
| **Logitech K400** | Keyboard/Touchpad | Works as a standard computer keyboard and touchpad. |

> [!TIP]
> **Looking for a compatible remote?** Use the keyword **"Air Mouse"** when searching on e-commerce platforms. These devices usually support HID standards (USB/Bluetooth), providing better compatibility and a more seamless "Plug & Play" experience with Q-TV.
>
> **Why choose an Air Mouse?** Models like the **G20S Pro** make navigating Q-TV's "app-first" interface easier without requiring a traditional computer mouse. A backlit version can also be useful when using Q-TV in low-light environments.


## Installation

Q-TV is currently in early development. Installation methods are focused on running from source.

For development setup instructions, please follow the guide in [CONTRIBUTING.md](CONTRIBUTING.md).

> [!TIP]
> Pre-built releases and official Q-TV images are planned for future releases.

## Roadmap

Q-TV is currently in **Early Development**. The roadmap may change as the project evolves and new requirements are discovered.

<details>
<summary>🚧 Current Focus</summary>



- Improve Q-TV Shell stability and user experience.
- Expand navigation system and TV-style interaction.
- Improve animations, layout, and overall interface polish.

</details>

<details>
<summary>📦 Planned</summary>


### Native Applications

Develop built-in Q-TV applications:

- Settings
- File Manager
- Q-TV Entertainment Center
- Q-TV Store

### Android TV Integration

- Integrate Android TV applications through Waydroid.
- Improve compatibility and user experience with Android TV apps.

### Q-TV Image

- Build an official Q-TV Image based on Fedora Minimal.
- Create a TV-focused Linux environment with simplified setup.
- Add first-time setup experience (OOBE).

</details>

<details>
<summary>🔮 Long Term Goals</summary>


- Support dedicated TV hardware and mini PC devices.
- Explore ARM64 support for compatible devices.
- Enable potential OEM and custom device integrations.
- Build a complete Linux-powered TV platform ecosystem.

</details>

## Languages
| Language Code | Language | Native Name | Translator | Note |
|---|---|---|---|---|
| en | English (US) | English | [nbao210](https://github.com/nbao210) | Primary & recommended |
| vi | Vietnamese | Tiếng Việt | [nbao210](https://github.com/nbao210) | 90% hoàn thiện |


## Contributing

Contributions are welcome! Whether you want to report bugs, suggest features, improve documentation, or contribute code, your help is appreciated.

Before contributing, please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide for development setup, coding guidelines, and pull request instructions.

> [!NOTE]
> Q-TV is currently in early development. Some features may change, be redesigned, or require discussion before implementation.

<div align="center">
    <p>Thanks to all Contributors</p>
<a href="https://github.com/nbao210/qtv-shell/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=nbao210/qtv-shell" />
</a>
</div>

## FAQ

<details>
<summary>What is Q-TV?</summary>

Q-TV is an open-source Smart TV platform that turns PCs and laptops into a TV-like experience using Linux.

It provides a TV-focused shell, native applications, and Android TV application support through Waydroid.

</details>

<details>
<summary>Is Q-TV a Linux distribution?</summary>

Not currently.

Q-TV is currently developed as a TV-focused shell and application platform. A dedicated Q-TV Image based on Fedora Minimal is planned for future releases.

</details>

<details>
<summary>Can I use Q-TV as my daily Smart TV system?</summary>

Q-TV is currently in early development and is intended for testing and development purposes.

A more complete experience will be available as the project matures.

</details>

<details>
<summary>Why does Q-TV use Linux instead of Android TV x86?</summary>

Q-TV uses Linux as its foundation to provide more flexibility, customization options, and broader hardware support.

Android TV applications can still be integrated through Waydroid when needed.

</details>

<details>
<summary>Can I run Android TV applications on Q-TV?</summary>

Yes, through Waydroid with an Android TV image.

Android TV application support is currently under development.

</details>

<details>
<summary>What hardware can run Q-TV?</summary>

Q-TV is designed to run on a wide range of hardware, including older PCs, laptops, and mini PCs.

See the [Requirements And Recommendations](#requirements-and-recommendations) section for recommended specifications.

</details>

<details>
<summary>Does Q-TV support Windows?</summary>

Windows support is not currently planned for the official Q-TV project.

Future ports or community-driven implementations may be possible.

</details>

<details>
<summary>Can I contribute to Q-TV?</summary>

Yes. Contributions are welcome!

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide before submitting issues or pull requests.

</details>

<details>
<summary>Can Q-TV revive my old PC?</summary>

Maybe! It depends on your hardware. Check the [Requirements And Recommendations](#requirements-and-recommendations) section to see if your old machine can handle Q-TV.

</details>

## License

<div align="center">

<p>Q-TV is licensed under the</p>

<a href="./LICENSE">
<img src="https://upload.wikimedia.org/wikipedia/commons/9/93/GPLv3_Logo.svg" alt="GPL-3.0 License" title="GPL-3.0 License" width="180"/>
</a>


**[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)**  
See [LICENSE](./LICENSE)

<a href="#top"><img src="https://img.shields.io/badge/Back to top-487E02?style=flat-square&logoColor=white" height="25"></a>

</div>



