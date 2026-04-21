# Developer Productivity Dashboard

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20mac-lightgrey)

A comprehensive desktop application that boosts developer productivity by combining essential tools into one clean, intuitive interface. Monitor system resources, generate secure passwords, organize messy folders, and manage notes—all from a single dashboard.

## 📸 Screenshot

*(Add a screenshot of your running application here)*
<img width="1366" height="768" alt="screenshot" src="https://github.com/user-attachments/assets/da1abc62-bc48-4612-8152-4bc6aecf8a05" />

## ✨ Features

### 📊 System Monitor
- **Real-time CPU usage** tracking with color-coded indicators
- **Live RAM usage** monitoring
- Auto-refresh every 2 seconds
- Visual percentage display

### 🔐 Password Generator
- Generate **strong, secure passwords** (12-16 characters)
- Includes uppercase, lowercase, digits, and symbols
- **Copy to clipboard** functionality
- Built with `secrets` module (cryptographically secure)

### 📁 File Organizer
- Automatically sort files into categorized folders
- Categories: Images, Documents, Videos, Music, Archives, Code, and more
- Safe moving with error handling
- Preview mode available

### 📝 Notes Manager
- Persistent notes storage using JSON
- Save and load notes between sessions
- Multi-line text area with scroll support
- Auto-save capability

### 🚀 Additional Features
- **Keyboard shortcuts** for power users
- **Cross-platform** support (Linux, Windows, Mac)
- **Clean, professional GUI** built with Tkinter

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core programming language |
| Tkinter | GUI framework |
| psutil | System monitoring |
| JSON | Data persistence |
| shutil | File operations |
| os | System interactions |
| secrets | Secure password generation |

## 📋 Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- pip package manager
- Git (optional, for cloning)

## 🚀 Installation

### 1. Clone the repository (or download ZIP)
```bash
git clone https://github.com/linuxhackwell/developer-productivity-dashboard.git
cd developer-productivity-dashboard
